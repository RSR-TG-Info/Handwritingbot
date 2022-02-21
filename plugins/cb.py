# ©️2022 RSR
from pyrogram import Client as RSR
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters


@RSR.on_callback_query()
async def button(client, message):

    cb_data = message.data
    if cb_data == "about":
        await message.answer("""
● 𝗡𝗮𝗺𝗲: Handwriting Bot
● 𝗖𝗿𝗲𝗮𝘁𝗼𝗿: RSR
● 𝗩𝗲𝗿𝘀𝗶𝗼𝗻: 1.0
● 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: Mongo DB
""", show_alert=True)
        
        

