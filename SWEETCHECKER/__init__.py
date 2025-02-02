import asyncio
import logging
import time
from importlib import import_module
from os import listdir, path
from dotenv import load_dotenv
from pyrogram import Client
from pyromod import listen
from config import API_ID, API_HASH, BOT_TOKEN, BOT_USERNAME, OWNER_ID, GPT_API, LOGGER_ID, DEEP_API

from SafoneAPI import SafoneAPI

safone = SafoneAPI()


loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



app = Client(
    ":SWEETCHECKER:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

scr = Client(
    "scr",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string="BQDfGfEAEKq6t_wJcVfHTBJy0wFXg1KjmDLt3xf4RutAuUendCVsgS3L3MIFEVLgca1RRE0IgP9owz6ldFpGzY2ogRTZCa_HuQihzr-sMdh-GQXDxWqL_Le1scsTXnjzd81Jxcg94MQRHqX_IIQ2QjCeYya4nTxq0FxESKeHMIEBGyrHqAG3_c28g7Q2HSx53RFLfBdy21ztu070wn8ZbtxgxikKbxAKAdHm8AWg_mwqBsfFIf3urPapkTPOpmC9tYSA_NR5M1Gg8I7xDu0aPTjs0tw7QeZ3s5t9aRJojO0gfpgQOdlT9m5g-dFYNNlf7Qtg-5LVl1lkqiFsErhIFSogYCN9ugAAAAGfWXZlAA"
)



async def info_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    await scr.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(info_bot())
