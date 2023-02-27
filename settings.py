import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def variables():
	return {
		"DISCORD_BOT_TOKEN": os.environ.get("DISCORD_BOT_TOKEN"),
		"TWILIO_ACCOUNT_SID": os.environ.get("TWILIO_ACCOUNT_SID"),
		"TWILIO_AUTH_TOKEN": os.environ.get("TWILIO_AUTH_TOKEN"),
		"TWILIO_NUMBER": os.environ.get("TWILIO_NUMBER"),
		"PERSONAL_NUMBER": os.environ.get("PERSONAL_NUMBER"),
	}