import os
import time
from json import JSONDecodeError

import requests

# import ffmpeg
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MashaRoBot.pyrogramee.pluginshelper import edit_or_reply, fetch_audio
from MashaRoBot import pbot


@pbot.on_message(filters.command("audify", prefixes=["/", "!"]))
async def shazamm(client, message):
    kek = await edit_or_reply(message, "`Load mek e...`")
    if not message.reply_to_message:
        await kek.edit("Audio emaw Video reply rawh")
        return
    if os.path.exists("friday.mp3"):
        os.remove("friday.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await kek.edit("**Zawng mek...**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await kek.edit("`He hla hi ka hmu zo lo`")
        return
    if not xo.get("success"):
        await kek.edit("`He hla hi ka hmu zo lo`")
        os.remove(downloaded_file_name)
        return
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    if not zzz:
        await kek.edit("`He hla hi ka hmu zo lo`")
        return
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    rsrkeyboa = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Hmu tu", url="https://t.me/tereuhtex_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/rsrbots"
                    )
                ],
            ]
        )
    messageo = f"""<b><u>Hla hmuh ani ✅</b></u>\n
<b>📁 Hla hming : </b> {title}\n
<b>🎙️ Sa/Siamtu : </b>{by}
"""
    await client.send_photo(message.chat.id, image, messageo, reply_markup=rsrkeyboa, reply_to_message_id=message.reply_to_message.message_id, parse_mode="HTML")
    os.remove(downloaded_file_name)
    await kek.delete()
