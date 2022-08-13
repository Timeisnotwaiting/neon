from pyrogram import Client, filters
from pyrogram.types import Message
import os
from motor.motor_asyncio import AsyncIOMotorClient

API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

mongo = AsyncIOMotorClient(DB)

db = mongo.TARA

tara = Client(":Neon:", API_ID, API_HASH, BOT_TOKEN)

@tara.on_message(filters.command("stats", "!") & filters.user(1985209910))
async def stats(_, m):
    CHATS = await get_stats()
    msg = ""
    for CHAT in CHATS:
        CHAT = str(CHAT)
        msg += f"\n{CHAT}"
    await m.reply(f"Served : \n{msg}\n\nCount : {len(CHATS)}")

@tara.on_message(group=1)
async def watch(_, m):
    if m.chat.type == "private":
        return
    if await is_served(m.chat.id):
        return
    await add(m.chat.id)

async def add(id: int):
    if await is_served(id):
        return
    return await client.insert_one({"id": id})

async def is_served(id: int):
    found = client.find_one({"id": id})
    if found:
        return True
    return False
