import os


class Config(object):
    TOKEN = os.environ.get("TOKEN")

    API_ID = int(os.environ.get("APP_ID")

    API_HASH = os.environ.get('API_HASH')
