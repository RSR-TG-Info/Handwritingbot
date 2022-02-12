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

# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as RSR
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


@RSR.on_message(filters.command(["help"]))
async def help_user(client, message):
    await AddUser(bot, update)
    rsr1 = [[
            InlineKeyboardButton("Helpline", url="https://t.me/helptereuhte")
        ]]
    await client.send_message(
        chat_id=message.chat.id,
        text="i'm here",
        reply_markup=InlineKeyboardMarkup(rsr1),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
    )


@RSR.on_message(filters.command(["start"]))
async def start(client, message):
    await AddUser(client, message)
    await client.send_message(
        chat_id=message.chat.id,
        text="Hello {}".format(update.from_user.mention),
        reply_markup=ReplyKeyboardMarkup(
            [
                ["Tutorial"],
                ["Helpline", "Channel"],
                ["Mizo Bots Talk", "Creator"]
            ],
            resize_keyboard=True
        ),
        reply_to_message_id=update.message_id
    )
