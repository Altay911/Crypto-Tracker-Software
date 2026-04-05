# 📈 Crypto Price Tracker & Alert Engine

A Python-based automation tool that monitors real-time cryptocurrency prices and dispatches secure email alerts when specific target thresholds are met.

## 💡 The Problem
Monitoring volatile crypto markets manually is inefficient. This project solves that by automatically polling live market data and proactively notifying the user, ensuring they never miss a critical trading window.

## 🛠️ Tech Stack
- **Language:** Python 3
- **APIs:** CoinGecko REST API (Real-time market data)
- **Security:** `python-dotenv` for secure environment variable management
- **Notifications:** `smtplib` / `email.message` for automated email dispatch
- **GUI (Testing):** Tkinter for local graphical interfaces

## 🧠 Key Features
- **Real-Time Polling:** Fetches live Ethereum/Crypto prices via HTTP requests.
- **Automated Alerts:** Sends instant email notifications when prices hit user-defined targets.
- **Secure Credentials:** Implements `.env` architecture to keep application passwords and API keys completely hidden from source control.

## ⚙️ How to Run Locally
1. Clone the repository: `git clone https://github.com/Altay911/Crypto-Tracker-Software.git`
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate it: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file in the root directory and add your Gmail App Password
6. Run the script: `python3 crypto_tracker.py`