# ©️2022 RSR
from pyrogram import Client as RSR


@RSR.on_callback_query()
async def button(client, message):

    cb_data = update.data
    if cb_data == "close":
        await message.message.delete()
    if cb_data == "hriattur":
        await update.answer("Zawn rei anih viau chuan i link rawn dah hi ka support lo tihna", show_alert=True)
        
    
