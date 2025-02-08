# Python UI - UI Entry Point

import tkinter as tk
from api_connector import checkout_equipment

def handle_checkout():
    user_id = 1
    equipment_id = 101
    response = checkout_equipment(user_id, equipment_id)
    label.config(text=response)

root = tk.Tk()
root.title("Equipment Checkout System")

button = tk.Button(root, text="Checkout Equipment", command=handle_checkout)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
