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


@RSR.on_message(filters.private & filters.command(["help"]))
async def help_user(client, message):
    await AddUser(client, message)
    rsr1 = [[
            InlineKeyboardButton("Developer", user_id="1060318977"),
            ]]
    await client.send_message(
        chat_id=message.chat.id,
        text="Send me a text, I'll convert to Handwriting. (Bot can't convert some languages)",
        reply_markup=InlineKeyboardMarkup(rsr1),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id
    )


@RSR.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    await AddUser(client, message)
    rsr2 = [[
            InlineKeyboardButton("Developer", user_id="1060318977")
            ],[
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Source", url="https://github.com/RSR-TG-Info/Handwritingbot")
        ]]
    await client.send_message(
        chat_id=message.chat.id,
        text="Hello {}\n\nI am Handwriting converter Bot, send me any text, I'll convert to Handwriting. (Bot can't convert some languages)".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(rsr2),
        reply_to_message_id=message.message_id
    )
