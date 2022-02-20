import os
import time
from json import JSONDecodeError
import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MashaRoBot.pyrogramee.pluginshelper import edit_or_reply, fetch_audio
from pyrogram import Client as RSR


@RSR.on_message(filters.private & filters.audio & filters.video & filter.document)
async def shazam(client, message):
    kek = await edit_or_reply(message, "`Loading...`")
    if not message.reply_to_message:
        await kek.edit("Reply Audio or Video")
        return
    if os.path.exists("RSR.mp3"):
        os.remove("RSR.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await kek.edit("**Searching...**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await kek.edit("**Song not found**")
        return
    if not xo.get("success"):
        await kek.edit("**Song not found**")
        os.remove(downloaded_file_name)
        return
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    if not zzz:
        await kek.edit("**Song not found**")
        return
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    rsrkeyboa = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Shazamer", url="https://t.me/tereuhtex_bot"
                    )
                ],
            ]
        )
    messageo = f"""<b><u>Song Shazamed ✅</b></u>\n
<b>📁 Song name : </b> {title}\n
<b>🎙️ Artist : </b>{by}
"""
    await client.send_photo(message.chat.id, image, messageo, reply_markup=rsrkeyboa, reply_to_message_id=message.reply_to_message.message_id, parse_mode="HTML")
    os.remove(downloaded_file_name)
    await kek.delete()
