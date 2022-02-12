from pyrogram import Client
from database.imm import rsr
from pyrogram.types import Message
from config import Config

async def AddUser(client: Client, message: Message):
    if not await rsr.is_user_exist(message.from_user.id):
           await rsr.add_user(message.from_user.id)
           if Config.LOG_CHANNEL is not None:
            await client.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER \n\n➥**Name:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\n➥**ID:** {message.from_user.id}"
            ) 
