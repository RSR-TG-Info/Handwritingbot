# ÂŠī¸2022 RSR
from pyrogram import Client as RSR
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters


@RSR.on_callback_query()
async def button(client, message):

    cb_data = message.data
    if cb_data == "about":
        await message.answer("""
â đĄđŽđēđ˛: Handwriting Bot
â đđŋđ˛đŽđđŧđŋ: RSR
â đŠđ˛đŋđđļđŧđģ: 1.0
â đđŽđđŽđ¯đŽđđ˛: Mongo DB
""", show_alert=True)
        
        

