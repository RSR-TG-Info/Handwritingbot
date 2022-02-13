# ©️2022 RSR
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3


if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as RSR
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@RSR.on_message(filters.command(["help"]))
async def help_user(client, message):
    await AddUser(client, message)
    rsr1 = [[
            InlineKeyboardButton("Support", url="https://t.me/helptereuhte"),
            ],[
            InlineKeyboardButton("Channel", url="https://t.me/rsrbots")
        ]]
    await client.send_message(
        chat_id=message.chat.id,
        text="<b>Private:</b>\n\n● Send me song name or YouTube video link, i will download and upload for you.\n● Send me Video or Audio, i will recognise.\n\n<b>Group:</b>\n\n● Send me song name or YouTube video link after command, command is /down\n<b>Example:</b>\n/down Marshmello - Alone\nor\n/down <code>https://youtu.be/ALZHF5UqnU4</code>\n\n● Send me Video or Audio. Then, reply your vedio/audio with command, command is /audify.",
        reply_markup=InlineKeyboardMarkup(rsr1),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id
    )


@RSR.on_message(filters.command(["start"]))
async def start(client, message):
    await AddUser(client, message)
    rsr2 = [[
            InlineKeyboardButton("Help", callback_data="help")
            ],[
            InlineKeyboardButton("Support", url="https://t.me/helptereuhte"),
            InlineKeyboardButton("Channel", url="https://t.me/rsrbots")
            ],[
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Developer", user_id="1060318977")
        ]]
    await client.send_message(
        chat_id=message.chat.id,
        text="Hello {}\n\nI am YouTube uploader and song recogniser Bot. You can download YouTube videos and you can find song using me.".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(rsr2),
        reply_to_message_id=message.message_id
    )