# ©️2022 RSR

import os
import requests
from database.adduser import AddUser
from .fsub import ForceSub
from pyrogram import Client as RSR
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message



@RSR.on_message(filters.private & filters.text)
async def hwrite(client, message):
    await AddUser(client, message)
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    text = str(message.text)
    txt = await client.send_message(message.chat.id, text="`Making...`", reply_to_message_id=message.message_id)
    hmm = requests.post('https://api.single-developers.software/write', headers={'Content-Type': 'application/json'}, json={"text":f"{text}"}).history[1].url
    rsrkeyboards = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Bot", url="https://t.me/MZupbot"
                )
            ],
        ]
    )
    await client.send_chat_action(message.chat.id, "upload_photo")
    await client.send_photo(
        message.chat.id,
        photo=hmm,
        reply_markup=rsrkeyboards,
        reply_to_message_id=message.message_id
    )
    await txt.delete()
