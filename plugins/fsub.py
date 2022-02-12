# ©️2022 RSR

import asyncio
from config import Config
from pyrogram import Client as RSR
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(client: Client, message: Message):
    """
    Custom Pyrogram Based Telegram Bot's Force Subscribe Function by @rsrmusic.
    If User is not Joined Force Sub Channel Bot to Send a Message & ask him to Join First.
    
    :param bot: Pass Client.
    :param update: Pass Message.
    :return: It will return 200 if Successfully Got User in Force Sub Channel and 400 if Found that User Not Participant in Force Sub Channel or User is Kicked from Force Sub Channel it will return 400. Also it returns 200 if Unable to Find Channel.
    """
    
    try:
        invite_link = await client.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(client, message)
        return fix_
    except Exception as err:
        print(f"**{Config.UPDATES_CHANNEL} some error in forcesub**")
        return 200
    try:
        user = await client.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=message.from_user.id)
        if user.status == "kicked":
            await client.send_message(
                chat_id=message.chat.id,
                text="**Sorry, you're banned 🚫**",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=message.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await client.send_message(
            chat_id=message.chat.id,
            text="**You need to join my channel for use me, click** `Join` **button below**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join", url=invite_link.invite_link)
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=message.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(client, message)
        return fix_
    except Exception as err:
        print(f"**Some bugs in force sub**")
        return 200
