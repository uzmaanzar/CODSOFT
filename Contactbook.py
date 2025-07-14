import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# ---- Database Setup ----
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''
  CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT UNIQUE,
    email TEXT,
    address TEXT
  )
''')
conn.commit()

# ---- Core Functions ----
def refresh_list():
    lst.delete(0, tk.END)
    for row in c.execute("SELECT name, phone FROM contacts"):
        lst.insert(tk.END, f"{row[0]} — {row[1]}")

def add_contact():
    name = simpledialog.askstring("Name","Enter name:")
    phone = simpledialog.askstring("Phone","Enter phone:")
    email = simpledialog.askstring("Email","Enter email:")
    address = simpledialog.askstring("Address","Enter address:")
    if name and phone:
        try:
            c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?,?,?,?)",
                      (name, phone, email, address))
            conn.commit()
            refresh_list()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error","Phone must be unique")
    else:
        messagebox.showwarning("Missing","Name & phone required")

def delete_contact():
    sel = lst.get(tk.ACTIVE)
    if not sel: return
    name, phone = sel.split(" — ")
    if messagebox.askyesno("Confirm",f"Delete {name}?"):
        c.execute("DELETE FROM contacts WHERE phone=?", (phone,))
        conn.commit()
        refresh_list()

def search_contact():
    term = simpledialog.askstring("Search", "Name or phone:")
    if not term: return
    lst.delete(0, tk.END)
    q = f"%{term}%"
    for row in c.execute("SELECT name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?", (q,q)):
        lst.insert(tk.END, f"{row[0]} — {row[1]}")

def update_contact():
    sel = lst.get(tk.ACTIVE)
    if not sel: return
    name, phone = sel.split(" — ")
    new_name = simpledialog.askstring("Update name", "New name:", initialvalue=name)
    new_phone = simpledialog.askstring("Update phone", "New phone:", initialvalue=phone)
    new_email = simpledialog.askstring("Update email", "New email:")
    new_address = simpledialog.askstring("Update address", "New address:")
    if new_name and new_phone:
        try:
            c.execute("""UPDATE contacts SET name=?, phone=?, email=?, address=?
                         WHERE phone=?""",
                      (new_name, new_phone, new_email, new_address, phone))
            conn.commit()
            refresh_list()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error","New phone duplicates another record")
    else:
        messagebox.showwarning("Missing","Name & phone required")

# ---- GUI Setup ----
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")
lst = tk.Listbox(root, font=("Arial",12))
lst.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, pady=5)
for (txt, cmd) in [
    ("Add", add_contact),
    ("Update", update_contact),
    ("Delete", delete_contact),
    ("Search", search_contact),
    ("Refresh", refresh_list)
]:
    tk.Button(btn_frame, text=txt, command=cmd).pack(side=tk.LEFT, expand=True, padx=2)

refresh_list()
root.mainloop()
conn.close()
