from flask import Flask, request, jsonify, send_from_directory
from twilio.rest import Client
from dotenv import load_dotenv
import os
import datetime

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Twilio credentials from environment
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Store call logs
call_logs = []

@app.route('/')
def serve_ui():
    return send_from_directory('static', 'index.html')

@app.route('/make-call', methods=['POST'])
def make_call():
    data = request.get_json()
    number = data.get('number')

    try:
        call = client.calls.create(
            twiml='<Response><Say>This is an automated call from your Python bot. Goodbye!</Say></Response>',
            to=number,
            from_=twilio_number
        )

        log = {
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "number": number,
            "sid": call.sid,
            "status": "initiated"
        }
        call_logs.append(log)
        return jsonify(success=True, sid=call.sid)

    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/call-logs')
def get_logs():
    return jsonify(call_logs)

if __name__ == '__main__':
    app.run(debug=True)
