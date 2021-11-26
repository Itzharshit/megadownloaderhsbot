# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 123))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 1316963576))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """ Sorry can't hear you.
"""

  HELP_USER = """
I am Mega Downloader bot created by @pyrogrammers.

I can download files from mega.nz, Send me any link of mega.nz file and i will download it for you.I can also add caption for your file. You have to only reply your file with caption text, i will automatically add captions! 
"""

  START_TEXT = """
Hi {user_mention},

I'm Mega Downloader bot.
I can download files from mega.nz in your Telegram.
"""
