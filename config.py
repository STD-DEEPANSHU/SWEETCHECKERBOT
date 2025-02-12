
# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "28545924"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "5b8697a66d069daf771c03010659a2c0")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7542551291:AAG39dMD2g39CN3VgekHaAISGpRmg2o4rWE")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME", "SWEETCHECKER")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6656608288"))

EVAL = list(map(int, getenv("EVAL", "6656608288").split()))
# ------------------X------------------------------
DEEP_API = os.environ.get("DEEP_API", "96a36c8b-0a06-461a-bce3-851d5d997a60")
# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID", "-1001859571020"))
# ------------------------------------------------
GPT_API = os.environ.get("GPT_API", "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")
# ------------------------------------------------
DAXX_API = os.environ.get("DAXX_API", "5163c49d-b696-47f1-8cf9-")
# ------------------------------------------------
MONGO_DB = os.environ.get("CLONEDB", "mongodb+srv://DemonChatBot:DemonChatBot@demonchatbot.fnvs1.mongodb.net/?retryWrites=true&w=majority&appName=DemonChatBot")
