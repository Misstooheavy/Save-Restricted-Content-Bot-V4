# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27592877"))
API_HASH = getenv("API_HASH", "b079acad3e397d8fa153216d6eea9232")
BOT_TOKEN = getenv("BOT_TOKEN", "7883818164:AAG-kLWLefe-B95xbVXNrPtLvt6-PUybK0Q")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6949673056").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "1002379908212")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1373866049"))
