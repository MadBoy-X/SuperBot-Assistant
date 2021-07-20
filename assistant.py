from telethon import TelegramClient
import os

owner = os.environ.get("OWNER_ID", 1732236209)

TOKEN = os.environ.get("TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# kangers = os.environ.get("KANGERS_ID") 
# For using the above var, first add "KANGERS_ID" var in app.json (https://github.com/MadBoy-X/SuperBot-Assistant/blob/main/app.json) !!
# and then remove the "kangers" line from this code file (https://github.com/MadBoy-X/SuperBot-Assistant/blob/5d48b63f096c8bb14ade5b6a4cdee1cdff09b8e2/assistant.py#L20) !!

bot = TelegramClient ("madboyx", API_ID, API_HASH).start(bot_token=TOKEN)
devs = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
# bhaago bc kanger aya
photo = "https://telegra.ph/file/abe0d33ad14e6b36eb285.mp4"
abe = "https://telegra.ph/file/318b16f4ca867c290281a.png"

DEVS = [1732236209, 1511373882]

kangers = [1883752632, 1698803654, 1781874715, 1831780815, 1882919838, 1854565071, 1712612576, 1815892895, 1772470872, 1622398047, 1804823302, 1768714246, 1771499536, 1632162430]

from telethon import events, Button, custom
import asyncio
import logging
import os
from datetime import datetime
try:
  import requests
except:
  os.system("pip install requests")
try:
  import LEGENDX
except:
  os.system("pip install LEGENDX")
from requests import exceptions, get, post
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import re, sys, os

MADBOI = [[Button.url("Oᴡɴᴇʀ", "https://t.me/Warning_MadBoy_is_Back"), Button.url("Dᴇᴠs", "https://t.me/ItS_PRaNAv_Xd")]]
MADBOI += [[Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/SuperBot_OT"), Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/SuperBot_SupportChat")]]
MADBOI += [[custom.Button.inline("¿ Rᴜʟᴇs ?", data="rules")]]

mboy= [[custom.Button.inline("¿ Rᴜʟᴇs ?", data="rules")]]

madb = [[custom.Button.inline("«« Bᴀᴄᴋ", data="back")]]

madboy = [[Button.url("Sᴘᴀᴍ", "https://t.me/SuperBot_Spam"), Button.url("Cʜᴀᴛ", "https://t.me/SuperBot_SupportChat")]]

import logging
import os
from datetime import datetime
from telethon import events
import requests
from requests import exceptions, get
from telethon.errors.rpcerrorlist import YouBlockedUserError

@bot.on(events.ChatAction)
async def handler(event):
  if event.user_joined:
    mad = await event.get_user()
    boy = mad.first_name
    gurl = mad.id
    boi = mad.username
    if mad.id in kangers:
      await bot.send_message(event.chat.id, f"**Oh nooo!!!\nBe alert a kanger __{boy}__ has just joined our chat.**\n**Let me inform @admins**\n\n**Perma Link to his Profile:** [{boy}](tg://user?id={gurl})")
      await bot.send_message("Heya Boss", f"**Sorry to disturb you sir!!\nBut a kanger just joined your chat..!!**\n\n**➥ Name:** {boy}\n**➥ Username:** @{boi}")
    elif event.chat_id == -1001342134554:
      await bot.send_file(event.chat_id, photo, caption=f"**Heya __{boy}__!! Welcome to 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕..\nMake sure that you read the group rules...**\n\n**Profile link:** [{boy}](tg://user?id={gurl})\n**User ID:** `{gurl}`", buttons=mboy)
    else:
      await bot.send_message(event.chat.id, f"**Heyy!!\nI'm a Modified and Advanced Assistant for SuperBot, Sorry to say that, but I only work in 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑵𝒆𝒕𝒘𝒐𝒓𝒌!.!**", buttons=madboy)
      

@bot.on(events.NewMessage(pattern="/start|/START|#start"))
async def assistant (event):
  if event.chat_id == -1001342134554:
    await bot.send_file(event.chat_id,abe, caption=f"**Heya!! I'm a Modified and Advanced Assistant for SuperBot.\nAn Advanced Group Manager for 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑵𝒆𝒕𝒘𝒐𝒓𝒌!.!**", buttons=MADBOI)
  else:
    await bot.send_message(event.chat.id, f"**Heyy!!\nI'm a Modified and Advanced Assistant for SuperBot, Sorry to say that, but I only work in 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑵𝒆𝒕𝒘𝒐𝒓𝒌!.!**", buttons=madboy)
    
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"help")))
async def help (event):
  await event.edit("__**My Owner iz Buzy making this, he've uploaded only a few things yet!! This feature will be available soon!!**__\n\n**~~ SOON ~~**")
  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help (event):
  gendu = event.sender.username
  await event.edit(f"**@{gendu} Here are the rules for 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕:**\n\n- `No Abusing.`\n- `Don't use/test any other UserBots here.`\n- `No Pornographic Content Upload.`\n- `Don't PM Devs. ~ Result : Block + Ban`\n- `We respect all languages, But use English/Hindi as language medium.`\n- `No Spamming. ~ For that, use our` **Spam Group : @SuperBot_Spam**\n- `No queries would be answered related to your Fork/Clone.`\n\n**⚠️ Ignore any of the Rules, and you'll get G-Ban + F-Ban.**\n\n**Till now, Only these Rules👀**\n\n**Enjoy, and feel free to ask queries/give suggestions/appeals regarding the SuperBot.**", buttons=madb)

  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back")))
async def back(event):
  global LEGEND

  await event.edit("**Heya!! I'm a Modified and Advanced Assistant for SuperBot.\nAn Advanced Group Manager for 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑵𝒆𝒕𝒘𝒐𝒓𝒌!.!**", buttons=MADBOI)
  
@bot.on(events.NewMessage(pattern="/rules|/RULES|#rules"))
async def assistant (event):
  if event.chat_id == -1001342134554:
     await bot.send_message(event.chat.id, "**... Click the Button below for getting the rules of the Group ...**",buttons=mboy)
  else:
     await bot.send_message(event.chat.id, f"**Heyy!!\nI'm a Modified and Advanced Assistant for SuperBot, Sorry to say that, but I only work in 𝑺𝒖𝒑𝒆𝒓𝑩𝒐𝒕 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑵𝒆𝒕𝒘𝒐𝒓𝒌!.!**", buttons=madboy)


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

if __name__ ==  '__main__':
  bot.run_until_disconnected()
