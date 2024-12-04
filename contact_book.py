import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required fields!")
        return

    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact {name} added successfully!")
    clear_entries()
    view_contacts()

def view_contacts():
    contact_list.delete(0, tk.END)
    if not contacts:
        contact_list.insert(tk.END, "No contacts available!")
    else:
        for name, details in contacts.items():
            contact_list.insert(tk.END, f"{name}: {details['Phone']}")

def search_contact():
    search_term = search_entry.get().strip()
    contact_list.delete(0, tk.END)
    if not search_term:
        messagebox.showerror("Error", "Enter a name or phone number to search!")
        return

    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term == details["Phone"]:
            contact_list.insert(tk.END, f"{name}: {details['Phone']} (Email: {details['Email']}, Address: {details['Address']})")
            found = True
    if not found:
        contact_list.insert(tk.END, "No matching contacts found.")

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to delete!")
        return

    selected_text = contact_list.get(selected[0])
    name = selected_text.split(":")[0].strip()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        view_contacts()

def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to update!")
        return

    selected_text = contact_list.get(selected[0])
    name = selected_text.split(":")[0].strip()
    if name in contacts:
        name_entry.insert(0, name)
        phone_entry.insert(0, contacts[name]["Phone"])
        email_entry.insert(0, contacts[name]["Email"])
        address_entry.insert(0, contacts[name]["Address"])
        del contacts[name]
        messagebox.showinfo("Info", f"Update details for {name} and click 'Add Contact'.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Set up the GUI
root = tk.Tk()
root.title("Contact Book")

# Input fields for adding/updating contacts
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons for actions
tk.Button(root, text="Add Contact", command=add_contact, width=15).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Update Contact", command=update_contact, width=15).grid(row=5, column=0, columnspan=2, pady=5)

# Search bar
tk.Label(root, text="Search:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
search_entry = tk.Entry(root, width=30)
search_entry.grid(row=6, column=1, padx=5, pady=5)
tk.Button(root, text="Search Contact", command=search_contact, width=15).grid(row=7, column=0, columnspan=2, pady=5)

# Contact List Display
contact_list = tk.Listbox(root, width=50, height=10)
contact_list.grid(row=8, column=0, columnspan=2, pady=10)

# Delete and View Buttons
tk.Button(root, text="Delete Contact", command=delete_contact, width=15).grid(row=9, column=0, pady=5)
tk.Button(root, text="View All Contacts", command=view_contacts, width=15).grid(row=9, column=1, pady=5)

# Run the application
root.mainloop()
