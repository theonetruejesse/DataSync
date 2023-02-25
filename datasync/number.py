from flask import Flask, request
from twilio import twiml

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']

	response = twiml.Response() # no idea
	response.message("Hello {}, you said: {}".format(number, message_body))
	return str(response)