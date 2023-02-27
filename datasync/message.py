from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    resp = MessagingResponse()
    resp.message('Hello {}, you said {}'.format(number, message_body))
    return str(resp)

# send message

import settings
from twilio.rest import Client

account_sid = settings.variables()['TWILIO_ACCOUNT_SID']
auth_token = settings.variables()['TWILIO_AUTH_TOKEN']
twilio_number = settings.variables()['TWILIO_NUMBER']
personal_number = settings.variables()['PERSONAL_NUMBER']

client = Client(account_sid, auth_token)

def send_message(b):
	message = client.messages \
									.create(
											body=b,
											from_=twilio_number,
											to=personal_number
									)
	print(message.sid)
        
	
