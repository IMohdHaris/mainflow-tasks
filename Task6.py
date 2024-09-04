import tkinter as tk
from tkinter import ttk
import sqlite3

class BillingSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.db = sqlite3.connect("billing.db")
        self.cursor = self.db.cursor()

        # Create tables if they don't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                total REAL,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        """)
        self.db.commit()

        # Create GUI components
        self.product_frame = tk.Frame(root)
        self.product_frame.pack()
        self.product_label = tk.Label(self.product_frame, text="Product:")
        self.product_label.pack(side=tk.LEFT)
        self.product_entry = tk.Entry(self.product_frame)
        self.product_entry.pack(side=tk.LEFT)
        self.product_add_button = tk.Button(self.product_frame, text="Add", command=self.add_product)
        self.product_add_button.pack(side=tk.LEFT)

        self.customer_frame = tk.Frame(root)
        self.customer_frame.pack()
        self.customer_label = tk.Label(self.customer_frame, text="Customer:")
        self.customer_label.pack(side=tk.LEFT)
        self.customer_entry = tk.Entry(self.customer_frame)
        self.customer_entry.pack(side=tk.LEFT)
        self.customer_add_button = tk.Button(self.customer_frame, text="Add", command=self.add_customer)
        self.customer_add_button.pack(side=tk.LEFT)

        self.billing_frame = tk.Frame(root)
        self.billing_frame.pack()
        self.billing_label = tk.Label(self.billing_frame, text="Billing:")
        self.billing_label.pack(side=tk.LEFT)
        self.billing_entry = tk.Entry(self.billing_frame)
        self.billing_entry.pack(side=tk.LEFT)
        self.billing_button = tk.Button(self.billing_frame, text="Generate Invoice", command=self.generate_invoice)
        self.billing_button.pack(side=tk.LEFT)

    def add_product(self):
        name = self.product_entry.get()
        price = float(self.product_entry.get())
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.db.commit()

    def add_customer(self):
        name = self.customer_entry.get()
        address = self.customer_entry.get()
        self.cursor.execute("INSERT INTO customers (name, address) VALUES (?, ?)", (name, address))
        self.db.commit()

    def generate_invoice(self):
        # TO DO: implement invoice generation logic
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSoftware(root)
    root.mainloop()