import os
os.system ("pip install telethon")
from telethon import TelegramClient

"""
owner = os.environ.get("OWNER_ID", None)
token = os.environ.get("TOKEN")
api_id = os.environ.get("API_ID", None)
api_hash = os.environ.get("API_HASH", None)
"""
api_id = "3249905"
api_hash = "ec7d3e4024ae97115b59e22dd6b4697c"
token = "1921340877:AAE8LD8aAJFhXWiiIcVGRkLeVWBfxYzbpQ8"
bot = TelegramClient ("legendx", api_id, api_hash).start(bot_token=token)
devs = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
# kanger aaya bhaago bc
photo = "https://telegra.ph/file/20befefff7900a6b2c26e.jpg"
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

PERU = [[Button.url("Repo", "https://github.com/ULTRA-OP/ULTRA-X"), Button.url("Channel", "t.me/UltraX_Support")]]
PERU += [[Button.url("Spam", "https://t.me/UltraX_Spam"), Button.url("Support", "t.me/t.me/UltraXChat")]]
PERU += [[custom.Button.inline("Rules", data="rules")]]

HMM= [[custom.Button.inline("Rules", data="rules")]]

hmm = [[custom.Button.inline("Back", data="back")]]

alain = [[Button.url("Support", "https://t.me/UltraX_Support"), Button.url("Chat", "t.me/UltraXChat")]]

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
    pro = await event.get_user()
    boy = pro.first_name
    if event.chat_id == -1001427249400:
      await bot.send_file(event.chat_id, photo, caption=f"**Hello {boy} welcome to UltraX Chat\nMake sure that you read the group rules...**", buttons=HMM)
    elif pro.id == 1082238780:
      await bot.send_message(event.chat.id, f"**Oh no!\nBe alert a shitty kanger {boy} has just joined chat.\nLet me inform @admins**")
    else:
      await bot.send_message(event.chat.id, f"**Hello mate\nI am UltraX Assistant, Sorry to say that i only work in UltraX network.**", buttons=alain)
      

@bot.on(events.NewMessage(pattern="/start|/START|ULTRA"))
async def assistant (event):
  if event.chat_id == -1001427249400:
    await bot.send_message(event.chat_id,"**Hello I am UltraX assitant.\nA simple group manager bot to manage UltraX network**", buttons=PERU)
  else:
    await bot.send_message(event.chat.id, f"**Hello mate\nI am UltraX Assistant, Sorry to say that i only work in UltraX network.**", buttons=alain)
    
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"help")))
async def help (event):
  await event.edit("Feature coming soon")
  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help (event):
  await event.edit(f"**Here are the rules for UltraXChat:**\n\n-`Don't use other userbots here.`\n-`Send the full logs if your bot crashes.`\n `No pm to devs, results in ban.`\n-`No phonographic content here.`\n-`Dont spam through bot commands.`", buttons=hmm)

  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back")))
async def back(event):
  global LEGEND

  await event.edit("**Hello I am UltraX assitant.\nA simple group manager bot to manage UltraX network**", buttons=PERU)
  
@bot.on(events.NewMessage(pattern="/rules|/RULES"))
async def assistant (event):
  if event.chat_id == -1001427249400:
     await bot.send_message(event.chat.id, "**Click below to check group rules**",buttons=hmm)
  else:
     await bot.send_message(event.chat.id, f"**Hello mate\nI am UltraX Assistant, Sorry to say that i only work in UltraX network.**", buttons=alain)


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

if __name__ ==  '__main__':
  bot.run_until_disconnected()
