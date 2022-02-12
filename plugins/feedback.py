# ©️2022 RSR
from pyrogram import filters
from pyrogram import Client as RSR
from config import Config


@RSR.on_message(filters.command('feedback'))
async def report(client, message):
        if message.reply_to_message:
            await client.send_message(chat_id=Config.OWNER_ID, text=f"<b>⭕️Feedback⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 ID:</b> <code>{message.chat.id}</code>")
            await client.forward_messages(chat_id=Config.OWNER_ID, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
            await message.reply_text("<b>✅ Feedback was send</b>")
        else:
            await message.reply_text("<b>Reply feedback message with command.</b>")
