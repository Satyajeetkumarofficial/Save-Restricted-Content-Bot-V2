# ---------------------------------------------------
# File Name: __init__.py
# Description: A Pyrogram bot for downloading files from Telegram channels or groups 
#              and uploading them back to Telegram.
# Author: Gagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Created: 2025-01-11
# Last Modified: 2025-09-11 (FloodWait fix by ChatGPT)
# Version: 2.0.6
# License: MIT License
# ---------------------------------------------------

import asyncio
import logging
import time
from pyrogram import Client
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN, STRING, MONGO_DB, DEFAULT_SESSION
from telethon import TelegramClient, errors
from motor.motor_asyncio import AsyncIOMotorClient

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

botStartTime = time.time()

# Main Pyrogram Bot
app = Client(
    "pyrobot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    parse_mode=ParseMode.MARKDOWN
)

# ✅ FloodWait safe Telethon start
async def start_telethon_session(session_name):
    while True:
        try:
            client = TelegramClient(session_name, API_ID, API_HASH)
            await client.start(bot_token=BOT_TOKEN)
            logging.info(f"{session_name} started successfully!")
            return client
        except errors.FloodWaitError as e:
            logging.warning(f"FloodWaitError: Waiting for {e.seconds} seconds before retrying {session_name}...")
            await asyncio.sleep(e.seconds + 5)

# Start telethon sessions safely
sex = loop.run_until_complete(start_telethon_session("sexrepo"))
telethon_client = loop.run_until_complete(start_telethon_session("telethon_session"))

# Optional extra client with string session
if STRING:
    pro = Client("ggbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)
else:
    pro = None

# Optional userbot session
if DEFAULT_SESSION:
    userrbot = Client("userrbot", api_id=API_ID, api_hash=API_HASH, session_string=DEFAULT_SESSION)
else:
    userrbot = None

# MongoDB setup
tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]  # Your database
token = tdb["tokens"]  # Your tokens collection

async def create_ttl_index():
    """Ensure the TTL index exists for the `tokens` collection."""
    await token.create_index("expires_at", expireAfterSeconds=0)

# Run the TTL index creation when the bot starts
async def setup_database():
    await create_ttl_index()
    logging.info("MongoDB TTL index created.")

async def restrict_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await setup_database()
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    BOT_NAME = f"{getme.first_name} {getme.last_name}" if getme.last_name else getme.first_name
    
    if pro:
        await pro.start()
    if userrbot:
        await userrbot.start()

loop.run_until_complete(restrict_bot())
