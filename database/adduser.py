from pyrogram import Client
from database.imm import rsr
from pyrogram.types import Message
from config import Config

async def AddUser(bot: Client, update: Message):
    if not await clinton.is_user_exist(update.from_user.id):
           await clinton.add_user(update.from_user.id)
           if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER \n\n➥**Name:** [{update.from_user.first_name}](tg://user?id={update.from_user.id})\n\n➥**ID:** {update.from_user.id}"
            ) 
