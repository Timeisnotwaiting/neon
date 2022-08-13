from pyrogram import Client, filters
from pyrogram.types import Message
import os
from motor.motor_asyncio import AsyncIOMotorClient

API_ID = 10763476
API_HASH = "e7d6d5493a896264a09d04fda7a30f9d"
BOT_TOKEN = "5379733874:AAFkOqgvhsKieb5jC3bsHt0tnvEG2UbmZd4"

DB = "mongodb+srv://alphaop:<password>@cluster0.0opks7r.mongodb.net/?retryWrites=true&w=majority"

mongo = AsyncIOMotorClient(DB)

db = mongo.TARA

client = db.client

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

async def get_stats():
    get_all = client.find({"id": {"$gt": 0}})
    if not get_all:
        return []
    LMAO = []
    for _ in await get_all.to_list(length=1000000000):
        LMAO.append(_["id"])
    return LMAO
