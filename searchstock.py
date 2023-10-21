

import tkinter as tk
from tkinter import ttk
import sqlite3

class ViewStock:
    def __init__(self, root):
        self.root = root
        self.root.title("Available Stock Details")
        self.root.geometry("1366x600+100+30")
        self.root.configure(bg="wheat")

        self.heading = tk.Label(root, text="Baby Garments & Shoes", font="arial 40 bold", bg="wheat", fg="black")
        self.heading.pack(pady=10)

        # Create an Entry widget for search
        self.search_entry = tk.Entry(root, width=100)
        self.search_entry.pack(pady=10)

        # Create a Search button
        search_button = tk.Button(root,width=23, text="Search Product by Name",font="arial 14 bold", command=self.search_data,bg="green", fg="white")
        search_button.pack(pady=5)

        # Create a Treeview widget
        self.tree = ttk.Treeview(root, show="headings", height=5)
        self.tree["columns"] = ("ID", "Name","Stock","Cost Price", "Sale Price", "Total Cost Price", "Total Sale Price", "Assumed Profit", "Vendor", "Vendor Phone")

        # Define column headings
        self.tree.column("ID", anchor=tk.W, width=50)
        self.tree.column("Name", anchor=tk.W, width=150)
        self.tree.column("Stock", anchor=tk.W, width=150)
        self.tree.column("Cost Price", anchor=tk.W, width=80)
        self.tree.column("Sale Price", anchor=tk.W, width=80)
        self.tree.column("Total Cost Price", anchor=tk.W, width=100)
        self.tree.column("Total Sale Price", anchor=tk.W, width=100)
        self.tree.column("Assumed Profit", anchor=tk.W, width=100)
        self.tree.column("Vendor", anchor=tk.W, width=100)
        self.tree.column("Vendor Phone", anchor=tk.W, width=100)

        # Set column headings
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Stock", text="Stock", anchor=tk.W)
        self.tree.heading("Cost Price", text="Cost Price", anchor=tk.W)
        self.tree.heading("Sale Price", text="Sale Price", anchor=tk.W)
        self.tree.heading("Total Cost Price", text="Total Cost Price", anchor=tk.W)
        self.tree.heading("Total Sale Price", text="Total Sale Price", anchor=tk.W)
        self.tree.heading("Assumed Profit", text="Assumed Profit", anchor=tk.W)
        self.tree.heading("Vendor", text="Vendor", anchor=tk.W)
        self.tree.heading("Vendor Phone", text="Vendor Phone", anchor=tk.W)

        # Add Treeview to the window
        self.tree.pack(padx=10, pady=10, expand=True, fill="both")

        # Connect to the database and fetch data
        self.conn = sqlite3.connect(database="Database/store.db")
        self.cursor = self.conn.cursor()
        self.show_data()

    def show_data(self):
        # Fetch data from the database and insert into the Treeview
        self.cursor.execute("SELECT * FROM inventory")
        data = self.cursor.fetchall()
        print(data)

        # Add a tag to alternate rows for better visibility
        for i, row in enumerate(data):
            tags = "oddrow" if i % 2 == 1 else "evenrow"
            reordered_data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9])
            # print(reordered_data)
            self.tree.insert("", "end", values=reordered_data, tags=(tags,))

        # Configure tag colors
        self.tree.tag_configure("oddrow", background="#f0f0f0")
        self.tree.tag_configure("evenrow", background="#e0e0e0")

    def search_data(self):
        # Clear existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch and display data based on the search term
        search_term = self.search_entry.get()
        self.cursor.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + search_term + '%',))
        data = self.cursor.fetchall()

        for i, row in enumerate(data):
            tags = "oddrow" if i % 2 == 1 else "evenrow"
            reordered_data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[8], row[7])
            self.tree.insert("", "end", values=reordered_data, tags=(tags,))

        # Configure tag colors
        self.tree.tag_configure("oddrow", background="#f0f0f0")
        self.tree.tag_configure("evenrow", background="#e0e0e0")

def main():
    root = tk.Tk()
    app = ViewStock(root)
    root.mainloop()
if __name__ == "__main__":
    main()
