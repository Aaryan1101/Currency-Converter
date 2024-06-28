import tkinter as tk
from tkinter import messagebox
import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {data['error-type']}")
    
    if 'conversion_rates' not in data:
        raise Exception("Error: 'conversion_rates' not found in response data.")
    
    rates = data['conversion_rates']
    
    if target_currency not in rates:
        raise Exception(f"Currency {target_currency} not found in exchange rates.")
    
    return rates[target_currency]

def convert_currency(amount, rate):
    return amount * rate

def convert_currency_callback():
    try:
        api_key = 'd90ac71826e3f7ece4cf1296'
        base_currency = base_currency_entry.get().upper()
        target_currency = target_currency_entry.get().upper()
        amount = float(amount_entry.get())
        
        rate = get_exchange_rate(api_key, base_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        result_label.config(text=f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Currency Converter")

base_currency_label = tk.Label(root, text="Base Currency:")
base_currency_label.pack()
base_currency_entry = tk.Entry(root, width=40)
base_currency_entry.pack()

target_currency_label = tk.Label(root, text="Target Currency:")
target_currency_label.pack()
target_currency_entry = tk.Entry(root, width=40)
target_currency_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root, width=40)
amount_entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert_currency_callback)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()