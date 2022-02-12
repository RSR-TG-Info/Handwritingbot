import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    # database session name, example: xurluploader
    DATABASE_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    #log channel
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    #update channel
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
