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
    session_string="BQGzk4QASExOHVEaTjtApUAE0tvOVzzF6fu75hAVm9JI0GHJC8jGwbE3wLm9FrJ70WUAmMDXAhr2ZagsLl35LgX2b8k_rIs1_nt8iR9QVsvnkOvuw3VCoR5hKq3kdzI-c-06lFMwZRqetoHxWt6Xls4b6iWbX8qR05slqfmaffpyEbW5DfOedbU2o0tSI-p5XB9vSTB_nXqxGMap3b3HMymSkThiIqeVL0vzKyxKk2kLvueX2wZY-5522TxatrRJTkH1Vbd1jRsRMHgau3KtWajIt_1fy0DFp-MwXsKIU7uP32Vbc8qvC8RM-rg9pDHiC-SK2mDFsw--b9HRD1Idxc2vCsThKgAAAAF07LXSAA"
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
