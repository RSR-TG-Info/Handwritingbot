# ©️2022 RSR
from pyrogram import Client as RSR


@RSR.on_callback_query()
async def button(client, message):

    cb_data = update.data
    if cb_data == "close":
        await message.message.delete()
    if cb_data == "hriattur":
        await message.answer("Zawn rei anih viau chuan i link rawn dah hi ka support lo tihna", show_alert=True)
    if cb_data == "start":
        rsr3 = [[
            InlineKeyboardButton("Help", callback_data="help"),
            ],[
            InlineKeyboardButton("Support", url="https://t.me/helptereuhte"),
            InlineKeyboardButton("Channel", url="https://t.me/rsrbots"),
            ],[
            [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Developer", user_id="1060318977"),
        ]]
        reply_markup = InlineKeyboardMarkup(rsr3)
        await message.answer()
        await message.message.edit_text(
            text="Hello {}\n\n I am YouTube uploader and song recogniser.".format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
    if cb_data == "help":
        rsr4 = [[
            InlineKeyboardButton("Back", callback_data="start"),
        ]]
        reply_markup = InlineKeyboardMarkup(rsr4)
        await message.answer()
        await message.message.edit_text(
            text="*Private:*\n\n● Send me song name or YouTube link, i will download and upload for you.\n● Send me Video or Audio, i will recognise.\n\n*Group:*\n\n● Send me song name or YouTube video link after command, command is /down\n*Example:*\n/down Marshmello - Alone\nor\n/down https://youtu.be/ALZHF5UqnU4\n\n● Send me Video or Audio. Then, reply your vedio/audio with command, command is /audify.",
            reply_markup=reply_markup,
            parse_mode='html'
    if cb_data == "about":
        await message.answer("""
● 𝗛𝗺𝗶𝗻𝗴: Mizo Movies
● 𝗦𝗶𝗮𝗺𝘁𝘂: RSR
● 𝗩𝗲𝗿𝘀𝗶𝗼𝗻: 1.1
● 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: Mongo DB
""", show_alert=True)
    
