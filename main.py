import settings
import datasync.bot as bot
import datasync.message as message

#  cant run both, single threaded processes
if __name__ == "__main__":
    # token = settings.variables()["DISCORD_BOT_TOKEN"]
    # bot.run_discord_bot(token)

    message.app.run()
    # 1. run the following: ~/ % ./ngrok http 5000
    # 2. make sure ngrok link is the same as twilio webhook

