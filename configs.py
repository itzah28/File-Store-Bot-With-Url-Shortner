import os

class Config(object):
  API_ID = int(os.environ.get("29361361", ""))
  API_HASH = os.environ.get("40314fdb92f99d22a1a84f4976f93913", "")
  BOT_TOKEN = os.environ.get("7496617418:AAEOjfGhwWX1GtO_6WeYnuaVOt9dw6tIkQk", "")
  BOT_USERNAME = os.environ.get("@itzahbot", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('udlinks.com', "")
  SHORTLINK_API = os.environ.get('f5098f0d8b30285321147c63d99c545e047ba53c
', "")
  BOT_OWNER = int(os.environ.get("6187813986", ""))
  DATABASE_URL = os.environ.get("mongodb+srv://adilaqbalhoda012:adil@123@cluster0.lzueu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
  UPDATES_CHANNEL = os.environ.get("1002215534933", "")
  LOG_CHANNEL = int(os.environ.get("1002215534933", ""))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [AH](https://www.instagram.com/itzah28/?hl=en)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
