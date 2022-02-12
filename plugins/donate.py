# ©️2022 RSR
from pyrogram import filters
from pyrogram import Client as RSR



@RSR.on_message(filters.command("donate")
async def donate(client, message):
  await client.forward_messages(message.chat.id, from_chat_id=-1001640035413, message_ids=30)
  
  
