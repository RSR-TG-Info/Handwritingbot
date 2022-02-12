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
        buttons = [[
            InlineKeyboardButton('Help', callback_data='help')
            ],[
            InlineKeyboardButton('Helpline', url='https://t.me/helptereuhte'),
            InlineKeyboardButton('Channel', url='https://t.me/rsrbots')
            ],[
            InlineKeyboardButton('Developer', user_id='1060318977'),
            InlineKeyboardButton('About', callback_data='about')
            ],[
            InlineKeyboardButton('Share', url='https://t.me/share/url?url=Mizo%20%E1%B9%ADawnga%20lehlin%20movie%20%E1%B9%ADhenkhat%20zawn%20na%20leh%20en%20na%20hi%20i%20hman%20ve%20duh%20chuan%20a%20hnuaia%20Bot%20tia%20ka%20kawh%20na%20zawn%20a%20username%20khu%20hmet%20la%20i%20hmang%20thei%20ang%2C%20a%20free%20vek%20in.%0A%0ABot%20%F0%9F%91%89%20%40mzmvbot')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.answer()
        await message.message.edit_text(
            text="Hello {}\n\n I am YouTube uploader and song recogniser.".format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
    
