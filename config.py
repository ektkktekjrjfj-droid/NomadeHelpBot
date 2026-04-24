# ============================================================
#Group Manager Bot
# Author: LearningBotsOfficial (https://t.me/+dPlNdXZ0SnxmMDE1) 
# Support: https://t.me/+dPlNdXZ0SnxmMDE1
# Channel: https://t.me/kushal_igcc_chats
# YouTube: https://www.youtube.com/@kushalzxgamer
# License: Open-source (keep credits, no resale)
# ============================================================

import os
from dotenv import load_dotenv

load_dotenv()

# Required configurations
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

OWNER_ID = int(os.getenv("OWNER_ID", 0))
BOT_USERNAME = os.getenv("BOT_USERNAME", "NomadeHelpBot")

SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/kushal_igcc_chats")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/+dPlNdXZ0SnxmMDE1")
START_IMAGE = os.getenv("START_IMAGE", "https://t.me/+dPlNdXZ0SnxmMDE1")
