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
    session_string="BQGbk2AAlLj1v-R-Ygb_U3NduCc7RNM-TJoqfxMvQtqU9KfP2pFlw24S4sRCWAV8rSvDjITAY-GNwuUTJQlcehA2T8XgF4sQwAO5fRUVHMmVZBQa2YMW8binIaSRWFaJQD1t2W0kPCV9zWh20rQe_SJ58sgvkHefR1FkqTbtVJl-T5RAOOSV9r-1y2MGsbaU_UBmVALTCUpdUUXHKgtM42Lpmw8b9zQdGVQuyjl7oyqbmy6k9QS1vA3CQ8ybv7Voyj5bG5Q-pfULeGKERQTFC1z1E6sDWIe8sf6EXnY8oSNZW4yirjYPAGKcryv_B5GPjzyM4GhH977vDkTFS5Jkj-PNxxf8_wAAAAGfWXZlAA"
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
