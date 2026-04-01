import requests
import time
import os
import smtplib
import tkinter as tk
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SENDER = "educationvideos13@gmail.com"
RECEIVER = "educationvideos13@gmail.com"
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
TARGET_PRICE = 2200
URL = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'

is_tracking = False
response = requests.get(URL)
data = response.json()
current_price = data['ethereum']['usd']

def send_email(price):
    msg = EmailMessage()
    msg['Subject'] = "ALERT FROM CRYPO BOT! URGENT!!!"
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    msg.set_content(f"Alert! Ethereum has hit your target: ${TARGET_PRICE} and right now the price is: ${current_price}")
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER, PASSWORD)
        smtp.send_message(msg)
    
    print("Alert has sent to your email, check inbox and spam folder.")

def log_csv(price):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("ethereum_history.csv", "a") as file:
        file.write(f"{now} ${price}\n")

print(f"Tracking Ethereum... waiting for it to hit {TARGET_PRICE}")

def fetch_and_update():
    try:
        response = requests.get(URL)
        data = response.json()
        current_price = data['ethereum']['usd']

        print(f"current price: {current_price}")
        
        price_label.config(text=f"${current_price}")

        log_csv(current_price)

        if current_price >= TARGET_PRICE:
            print("🚨 TARGET HIT! 🚨")
            os.system(f" say 'Alert! Ethereum price just hit {current_price} dollars!'")
            send_email(current_price)
            toggle_tracking()
            price_label.config(fg="#00ff00")

    except Exception as e:
        price_label.config(text="API Error")
        print(f"Error Occurred: {e}")
              

    if is_tracking:
        root.after(20000, fetch_and_update)


def toggle_tracking():
    global is_tracking

    if not is_tracking:
        is_tracking = True
        start_button.config(text="Stop Tracking!")
        fetch_and_update()
    else:
        is_tracking = False
        start_button.config(text="Start Tracking")
        price_label.config(text="$---", fg="white")

root = tk.Tk()
root.title("Crypto Tracker Pro")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="Ethereum Live Price", font=("Helvetica", 16), fg="white", bg="#1e1e1e")
title_label.pack(pady=20)

price_label = tk.Label(root, text="$---", font=("Helvetica", 54, "bold"), fg="white", bg="#1e1e1e")
price_label.pack(pady=20)

start_button = tk.Button(root, text="Simulate Price Alert", font=("Helvetica", 14), command=toggle_tracking)
start_button.pack(pady=20)

root.mainloop()