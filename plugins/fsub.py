# (c) @AbirHasan2005

import asyncio
from sample_config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, update: Message):
    """
    Custom Pyrogram Based Telegram Bot's Force Subscribe Function by @rsrmusic.
    If User is not Joined Force Sub Channel Bot to Send a Message & ask him to Join First.
    
    :param bot: Pass Client.
    :param update: Pass Message.
    :return: It will return 200 if Successfully Got User in Force Sub Channel and 400 if Found that User Not Participant in Force Sub Channel or User is Kicked from Force Sub Channel it will return 400. Also it returns 200 if Unable to Find Channel.
    """
    
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update)
        return fix_
    except Exception as err:
        print(f"**{Config.UPDATES_CHANNEL} force subscribe ah hian harsatna a awm**")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=update.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=update.chat.id,
                text="**A pawi khawp mai min hmang theilo tur a ban ini tlat**",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=update.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=update.chat.id,
            text="**Min hman i duh chuan a hnuai a** `Join` **tih button khu hmet la channel kha join phawt rawh, channel member te chauh in min hmang thei, i join zawh ah link kha min thawn nawn leh dawn nia.**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join", url=invite_link.invite_link)
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=update.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, update)
        return fix_
    except Exception as err:
        print(f"**Force Subscribe ah thil felhlelh a awm**")
        return 200
