from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

tara = Client(":Neon:", API_ID, API_HASH, BOT_TOKEN)

@tara.on_message(filters.command("stats", "!") & filters.user(1985209910))
async def stats(_, m):
    CHATS = get_stats()
    msg = ""
    for CHAT in CHATS:
        CHAT = str(CHAT)
        msg += f"\n{CHAT}"
    await m.reply(f"Served : \n{msg}\n\nCount : {len(CHATS)}")
