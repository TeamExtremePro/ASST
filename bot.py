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
token = "1878316063:AAEnEyFVq4WK_1LpSg1gFMqfYDG0via44tA"
bot = TelegramClient ("amanpandey", api_id, api_hash).start(bot_token=token)
devs = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
# kanger aaya bhaago bc
photo = "https://telegra.ph/file/3d208ecf6d0ea9389d8f8.jpg"
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

PERU = ("Repo", "https://github.com/Noob-Stranger/andencento"), ("Channel", "t.me/Andencento")
PERU += ("Spam", "Coming soon"), Button.url("Support", "t.me/AndencentoSupport")

HMM= [[custom.Button.inline("Rules", data="rules")]]

hmm = [[custom.Button.inline("Back", data="back")]]

aman = [[Button.url("Repo", "https://github.com/Noob-Stranger/andencento"), Button.url("Chat", "t.me/AndencentoSupport")]]

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
    if event.chat_id == -1001313453168:
      await bot.send_file(event.chat_id, photo, caption=f"**Hello {boy} welcome to Andencento Chat\nMake sure that you read the group rules...**", buttons=HMM)
    elif pro.id == 1082238780:
      await bot.send_message(event.chat.id, f"**Oh no!\nBe alert a shitty kanger {boy} has just joined chat.\nLet me inform @admins**")
    else:
      await bot.send_message(event.chat.id, f"**Hello mate\nI am Andencento Assistant, Sorry to say that i only work in Andencento network.**", buttons=aman)
      

@bot.on(events.NewMessage(pattern="/start|/START|ANDENCENTO"))
async def assistant (event):
  if event.chat_id == -1001313453168:
    await bot.send_message(event.chat_id, f"**Hello sir\nI am Andencento assitant.\nA simple group manager bot to manage Andencento network**", buttons=aman)
  else:
    await bot.send_message(event.chat.id, f"**Hello sir\nI am Andencento Assistant, Sorry to say that i only work in Andencento network.**", buttons=aman)
    
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"help")))
async def help (event):
  await bot.send_message("Feature coming soon")
  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help (event):
  await bot.send_message(f"**Here are the rules for Andencento Support:**\n\n-`Don't use other userbots here.`\n-`Send the full logs if your bot crashes.`\n `No pm to devs, results in ban.`\n-`No phonographic content here.`\n-`Dont spam through bot commands.`", buttons=HMM)

  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back")))
async def back(event):
  global AMAN

  await bot.send_message("**Hello I am ANDENCENTO assitant.\nA simple group manager bot to manage ANDENCENTO network**", buttons=aman)
  
@bot.on(events.NewMessage(pattern="/rules|/RULES"))
async def assistant (event):
  if event.chat_id == -1001313453168:
     await bot.send_message(event.chat.id, "**Click below to check group rules**",data=rules)
  else:
     await bot.send_message(event.chat.id, f"**Hello mate\nI am Andencento Assistant, Sorry to say that i only work in Andencento network.**", buttons=aman)


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


print ("Assistant Working Fine")
if __name__ ==  '__main__':
  bot.run_until_disconnected()
