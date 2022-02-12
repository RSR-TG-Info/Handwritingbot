
# ©️2022 RSR
import speedtest
import traceback
import os
from pyrogram.types import Message
from pyrogram import Client as RSR
from pyrogram import filters

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from database.imm import rsr

@RSR.on_message(filters.command('users'))
async def stats(client, message):
    if m.from_user.id != Config.OWNER_ID:
        return 
    total_users = await rsr.total_users_count()
    await message.reply_text(text=f"Total user(s) {total_users}", quote=True)


    

    
@RSR.on_message(filters.command('speedtest'))   
async def speedtest(client, message):
    msg = await message.reply_text("`Processing...`")
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    img_ = s.results.share()
    _neat_test = f"""<b><u>SPEED TEST</b></u>
    
▶ <b>IP :</b> <code>{client_infos['ip']}</code>
▶ <b>ISP :</b> <code>{client_infos['isp']}</code>
▶ <b>Country :</b> <code>{client_infos['country']}</code>
▶ <b>Download Speed :</b> <code>{convert_from_bytes_to_human_formats(download_speed)}</code>
▶ <b>Upload Speed :</b> <code>{convert_from_bytes_to_human_formats(upload_speed)}</code>
▶ <b>ISP RATING :</b> <code>{client_infos['isprating']}</code>
▶ <b>PING TIME :</b> <code>{ping_time}</code>
"""
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            reply_to_message_id=message.message_id,
            text=_neat_test,
            parse_mode="html"
        )
    else:
        await client.send_message(
            message.chat.id,
            text=_neat_test,
            parse_mode="html"
            )
    await msg.delete()
  


def convert_from_bytes_to_human_formats(size):
    power = 2**10
    n = 0
    units = {
        0: "",
        1: "KB",
        2: "MB",
        3: "GB",
        4: "TB"
    }
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"
