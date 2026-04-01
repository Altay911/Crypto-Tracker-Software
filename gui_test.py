import tkinter as tk

def test_button():
    price_label.config(text="$3500", fg="#00ff00")
    print("button clicked!")

root = tk.Tk()
root.title("Crypto Tracker Pro")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="Ethereum Live Price", font=("Helvetica", 16), fg="white", bg="#1e1e1e")
title_label.pack(pady=20)

price_label = tk.Label(root, text="$---", font=("Helvetica", 54, "bold"), fg="white", bg="#1e1e1e")
price_label.pack(pady=20)

start_button = tk.Button(root, text="Simulate Price Alert", font=("Helvetica", 14), command=test_button)
start_button.pack(pady=20)

root.mainloop()