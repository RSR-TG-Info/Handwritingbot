# ©️2022 RSR
from pyrogram import Client as RSR
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters


@RSR.on_callback_query()
async def button(client, message):

    cb_data = message.data
    if cb_data == "close":
        await message.message.delete()
    elif cb_data == "hriattur":
        await message.answer("Zawn rei anih viau chuan i link rawn dah hi ka support lo tihna", show_alert=True)
        return
    elif cb_data == "stut":
        rsr3 = [[
            InlineKeyboardButton("Help", callback_data="help")
            ],[
            InlineKeyboardButton("Support", url="https://t.me/helptereuhte"),
            InlineKeyboardButton("Channel", url="https://t.me/rsrbots")
            ],[
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Developer", user_id="1060318977")
        ]]
        reply1 = InlineKeyboardMarkup(rsr3)
        await message.answer()
        await message.message.edit_text(
            text="Hello {}\n\nI am YouTube uploader and song recogniser Bot. You can download YouTube videos and you can find song with me.".format(message.from_user.mention),
            reply_markup=reply1,
            parse_mode='html'
        )
    elif cb_data == "help":
        rsr4 = [[
            InlineKeyboardButton("Back", callback_data="stut")
        ]]
        reply2 = InlineKeyboardMarkup(rsr4)
        await message.answer()
        await message.message.edit_text(
            text="**Private:**\n\n● Send me song name or YouTube video link, i will download and upload for you.\n● Send me Video or Audio, i will recognise.\n\n**Group:**\n\n● Send me song name or YouTube video link after command, command is /down\n**Example:**\n/down Marshmello - Alone\nor\n/down `https://youtu.be/ALZHF5UqnU4`\n\n● Send me Video or Audio. Then, reply your vedio/audio with command, command is /audify.",
            reply_markup=reply2,
            disable_web_page_preview=True,
            parse_mode='markdown'
        )
    elif cb_data == "about":
        await message.answer("""
● 𝗛𝗺𝗶𝗻𝗴: MZup Bot
● 𝗖𝗿𝗲𝗮𝘁𝗼𝗿: RSR
● 𝗩𝗲𝗿𝘀𝗶𝗼𝗻: 1.0
● 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: Mongo DB
""", show_alert=True)
        
        
@RSR.on_callback_query(filters.regex("forceclose"))
async def forceclose(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    await CallbackQuery.message.delete()
    await CallbackQuery.answer()

@RSR.on_callback_query(filters.regex("forceclosed"))
async def forceclose(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "You're not allowed to close this.", show_alert=True
        )
    await CallbackQuery.message.delete()
    await CallbackQuery.answer()
