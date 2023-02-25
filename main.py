import settings
import datasync.bot as bot

if __name__ == "__main__":
    token = settings.variables()["DISCORD_BOT_TOKEN"]
    bot.run_discord_bot(token)
