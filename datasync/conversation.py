import settings
from twilio.rest import Client

account_sid = settings.variables()['TWILIO_ACCOUNT_SID']
auth_token = settings.variables()['TWILIO_AUTH_TOKEN']
twilio_number = settings.variables()['TWILIO_NUMBER']
personal_number = settings.variables()['PERSONAL_NUMBER']

client = Client(account_sid, auth_token)

def create_conversation():
	conversation = client.conversations \
                     .v1 \
                     .conversations \
                     .create(friendly_name='My First Conversation')
	conversation_sid = conversation.sid
	print(conversation_sid)

	c = client.conversations \
                     .v1 \
                     .conversations(conversation_sid) \
                     .fetch()
	print(c.chat_service_sid)

	p = client.conversations \
    .v1 \
    .conversations(conversation_sid) \
    .participants \
    .create(
         messaging_binding_address=personal_number,
         messaging_binding_proxy_address=twilio_number
     )
	print(p.sid)