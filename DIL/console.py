import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt",
            maxBytes=(1024 * 1024 * 5),
            backupCount=10
        ),
        logging.StreamHandler(),
    ],
)


logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


if os.path.exists("Internal"):
    load_dotenv("Internal")


API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

STRING_SESSION = getenv("STRING_SESSION", None)
SESSION_STRING = getenv("SESSION_STRING", None)

MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))


COMMAND_PREFIXES = list(
    getenv("COMMAND_PREFIXES", ". ! s").split()
)


PM_GUARD = bool(
    getenv("PM_GUARD", True)
)

PM_GUARD_TEXT = getenv(
    "PM_GUARD_TEXT",
    "**Hᴇʏ ᴛʜᴇʀᴇ! I'ᴍ ᴀ sᴍᴀʀᴛ ᴀɴᴅ ғᴀsᴛ ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ.**"
)

PM_GUARD_LIMIT = int(
    getenv("PM_GUARD_LIMIT", 5)
)


USERBOT_PICTURE = getenv(
    "USERBOT_PICTURE",
    "https://te.legra.ph/file/6926207a8c9c4b8e4b93c.jpg"
)


LOGGER = logging.getLogger("DIL")

runtime = time.time()


FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}

PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []

for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)

COMMAND_HANDLERS.append("")
