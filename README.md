# 📲 Twilio SMS Sender (Flask + HTML UI)

Send SMS messages worldwide using Twilio's SMS API, powered by a simple Flask backend and a sleek HTML/CSS frontend.

---

## ✨ Features

- 🔐 Send SMS messages via Twilio
- 🌐 Clean and responsive HTML/CSS UI
- ⚙️ Built with Flask
- 💬 Real-time feedback on delivery status
- 🗂️ Logs sent messages (optional feature)

---


## 🚀 Tech Stack

| Technology | Use |
|------------|-----|
| [Flask](https://flask.palletsprojects.com/) | Web server |
| [Twilio](https://www.twilio.com/docs/sms) | SMS API |
| HTML + CSS | Frontend |
| JavaScript (Fetch API) | Client-server communication |

---

## 📁 Project Structure
```
twilio_sms_sender/
├── app.py             # Flask server
├── static/
│   └── index.html     # Frontend UI
└── README.md          # Project documentation


```

---

## 🛠️ Setup Instructions

### 1. 🔑 Twilio Setup

- Create an account at [Twilio](https://www.twilio.com/)
- Get:
  - **Account SID**
  - **Auth Token**
  - **Twilio Phone Number**

> ⚠️ Never expose your Twilio credentials in public code. Use `.env` in production.

---

### 2. 📦 Install Dependencies


pip install flask twilio
3. ▶️ Run the App

python app.py
Open http://localhost:5000 in your browser.

4. 🧪 Send a Test Message
Enter a valid phone number (e.g. +919876543210)

Type your message

Click 🚀 Send SMS

You’ll receive the SMS on your phone if the Twilio number supports the destination country.

📄 Sample .env (Recommended)

TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1xxxxxxxxxx
Then use it in app.py:


 Add message history UI

 Deploy to Render / Heroku

🙏 Acknowledgements
Twilio

Flask

You! 💙

📜 License
MIT License. Use freely with proper credit.


---

Let me know if you’d like this generated as a downloadable file (`README.md`) or need a deployment guide 
