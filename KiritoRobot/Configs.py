import os


class Config(object):
    APP_ID = os.environ.get("APP_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
    BOT_US = os.environ.get("BOT_US", "Devil_X_Robot")
    WELCOME_TEXT = os.environ.get(
        "WELCOME_TEXT", "Cardinal System Is Damaged!, Sorry I Cant Remember You."
    )
    RULES = os.environ.get("SUPPORT CHAT", "https://t.me/THEBLAZENETWORK")
