
# ©️2022 RSR
import speedtest
import traceback
import os
from pyrogram.types import Message
from pyrogram import Client as RSR
from pyrogram import filters

if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config
from database.imm import rsr

@RSR.on_message(filters.command('users'))
async def stats(client, message):
    if message.from_user.id != Config.OWNER_ID:
        return 
    total_users = await rsr.total_users_count()
    await message.reply_text(text=f"Total user(s) {total_users}", quote=True)


