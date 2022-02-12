from pyrogram import filters
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Helpline = "https://telegra.ph/file/7484d6814979032477998.jpg"
Channel = "https://telegra.ph/file/a23f335a8e6c50d37f164.jpg"
Mizo = "https://telegra.ph/file/66a6653e642dfffbcb4f5.jpg"
Creator = "https://telegra.ph/file/fe8bc24626585855fd752.jpg"



@Clinton.on_message(filters.private & filters.regex("Helpline"))
async def helpline(client, message):
  await client.send_photo(
    message.chat.id,
    Helpline,
    caption="Ka helpline group hi min hmandan emaw keimah a felhleh i thlen na tur ania, i awm duh chuan a hnuai a join button khu hmet la i join dawn nia",
    reply_to_message_id=message.message_id,
    reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Join", url="https://t.me/helptereuhte")]]
    ),
 )
   
  
  
  
  
@Clinton.on_message(filters.private & filters.regex("Channel"))
async def channel(client, message):
  await client.send_photo(
    message.chat.id,
    Channel,
    caption="Ka Channel i Join/Follow duh chuan a hnuai a Join button hi i hmet mai dawn nia",
    reply_to_message_id=message.message_id,
    reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Join", url="https://t.me/rsrbots")]]
    ),
 )
    
  
  
  
@Clinton.on_message(filters.private & filters.regex("Mizo Bots Talk"))
async def mizo(client, message):
  await client.send_photo(
    message.chat.id,
    Mizo,
    caption="Mizo Bot siamtu leh hmangtu te inkawm khawmna group i join duh chuan a hnuai a join button hi hmet la i join dawn nia",
    reply_to_message_id=message.message_id,
    reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Join", url="https://t.me/mzbotstalk")]]
    ),
 )
    
  
  
  
  
  
@Clinton.on_message(filters.private & filters.regex("Creator"))
async def creator(client, message):
  await client.send_photo(
    message.chat.id,
    Creator,
    caption="Min siamtu i hriat duh chuan a hnuai a creator tih button khu i hmet dawn nia",
    reply_to_message_id=message.message_id,
    reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Creator", url="https://t.me/rsrmusic")]]
    ),
 )
 




@Clinton.on_message(filters.private & filters.regex("Tutorial"))
async def tutorial(client, message):
  rsr2 = [
            [
                InlineKeyboardButton("Telegraph", url="https://telegra.ph/𝗥𝗦𝗥-11-28-2"),
            ],
            [
                InlineKeyboardButton("YouTube", url="https://youtu.be/3THNv0R3GO4"),
            ],
         ]
  await client.send_message(
    message.chat.id,
    text="A hnuai a **Telegraph** tih button khu hmet la tah khan min hman dan a thu a chhiar tur a awm ang, **YouTube** tih kha i hmeh chuan min hman dan video a en tur a awm ang.",
    reply_markup=InlineKeyboardMarkup(rsr2),
    reply_to_message_id=message.message_id
 )
