import os


class Config(object):
    TOKEN = os.environ.get("TG_BOT_TOKEN", None)

    API_ID = int(os.environ.get("APP_ID", None)

    API_HASH = os.environ.get("API_HASH", None)
