# ©️2022 RSR
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os


if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config

from pyrogram import Client as RSR
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    plugins = dict(root="plugins")
    hmm = RSR(
        "@MZupbot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=RSR.plugins)
    hmm.run()
