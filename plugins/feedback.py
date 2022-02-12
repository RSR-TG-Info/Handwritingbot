from pyrogram import filters
from pyrogram import Client as Clinton
from sample_config import Config


@Clinton.on_message(filters.command('feedback'))
async def report(bot, message):
        if message.reply_to_message:
                                  await bot.send_message(chat_id=Config.OWNER_ID, text=f"<b>⭕️Putarte Feedback⭕️\n \n🧿 Name: {message.from_user.mention}\n🧿 User ID:</b> <code>{message.chat.id}</code>")
                                  await bot.forward_messages(chat_id=Config.OWNER_ID, from_chat_id=message.from_user.id, message_ids=message.reply_to_message.message_id)
                                  await message.reply_text("<b>✅ I feedback chu min siamtu hnen ah thawn ani e.</b>")
        else:
             await message.reply_text("<b>Command hmang hian i message thawn tur reply tur.</b>")
