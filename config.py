import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "MaDyY_y")
ALIVE_NAME = getenv("ALIVE_NAME", "# ' 𝑳𝒂 𝑹𝑹𝒆 𝑵 ⊁")
BOT_USERNAME = getenv("BOT_USERNAME", "LAR_EN_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Q_X_T_I")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "M_D_O_W")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "UXXHT")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/madi-205/lalala")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
