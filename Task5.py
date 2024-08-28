import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("USD Currency Converter")
        self.exchange_rates = self.fetch_exchange_rates()

        # Create input field for USD amount
        self.usd_amount_label = tk.Label(root, text="USD Amount:")
        self.usd_amount_label.grid(column=0, row=0)
        self.usd_amount_entry = tk.Entry(root)
        self.usd_amount_entry.grid(column=1, row=0)

        # Create dropdown menu for target currencies
        self.target_currency_label = tk.Label(root, text="Target Currency:")
        self.target_currency_label.grid(column=0, row=1)
        self.target_currency = tk.StringVar()
        self.target_currency.set("EUR")  # default value
        self.target_currency_menu = ttk.Combobox(root, textvariable=self.target_currency)
        self.target_currency_menu['values'] = list(self.exchange_rates.keys())
        self.target_currency_menu.grid(column=1, row=1)

        # Create button for performing conversion
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=1, row=2)

        # Create button for refreshing exchange rates
        self.refresh_button = tk.Button(root, text="Refresh Rates", command=self.refresh_exchange_rates)
        self.refresh_button.grid(column=1, row=3)

        # Create output field for converted amount
        self.converted_amount_label = tk.Label(root, text="Converted Amount:")
        self.converted_amount_label.grid(column=0, row=4)
        self.converted_amount = tk.StringVar()
        self.converted_amount_label_value = tk.Label(root, textvariable=self.converted_amount)
        self.converted_amount_label_value.grid(column=1, row=4)

    def fetch_exchange_rates(self):
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        return data['rates']

    def convert_currency(self):
        usd_amount = float(self.usd_amount_entry.get())
        target_currency = self.target_currency.get()
        exchange_rate = self.exchange_rates[target_currency]
        converted_amount = usd_amount * exchange_rate
        self.converted_amount.set(f"{converted_amount:.2f} {target_currency}")

    def refresh_exchange_rates(self):
        self.exchange_rates = self.fetch_exchange_rates()
        self.target_currency_menu['values'] = list(self.exchange_rates.keys())

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()