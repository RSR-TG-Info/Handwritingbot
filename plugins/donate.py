from pyrogram import filters
from pyrogram import Client 



@Client.on_message(filters.command("donate", prefixes=["/", "!"]))
def donate(client, message):
  client.forward_messages(message.chat.id, from_chat_id=-1001640035413, message_ids=30)
  client.send_message(message.chat.id, text="A chunga Donate tih button hi hmet la min ṭanpui na'n i donate thei ang. Emaw, a hnuaia link hi join la, tah khan donate dan chidang deuh pawh a en theih ang.\n\nhttps://t.me/teamtereuhte", reply_to_message_id=message.message_id, disable_web_page_preview=True)
  
