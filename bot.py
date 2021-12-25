# You can customise your welcome message while deploying this bot 
# All Copyright © goes to SaminSumesh
# GNU LICENSE V3 Under Public Source



import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
"Simple Welcome Bot",
bot_token=os.environ.get("BOT_TOKEN"),
api_id=int(os.environ.get("API_ID")),
api_hash=os.environ.get("API_HASH")
)


GROUP = os.environ.get("GROUP")
WELCOME_MESSAGE = os.environ.get("WELCOME_MESSAGE")

# ---------------------------------*--------------------------------
# Button
START_TXT = """
HI {} , Test Run 1"""

ABOUT_TXT = """
🤖 Bot Name: Welcome Bot

📝 Language : Python 3

📚 Framework : Pyrogram

📡 Hosted On : Heroku

👨‍💻 Developer : [🇬🇧 Samin Sumesh](https://t.me/Paulwalker_tg)

💡 Source Code : [Click Here](https://github.com/saminsumesh/welcome-bot)

👥 Support Group : [XD Bots Support](https://t.me/xd_botzsupport)

📢 Updates Channel : [XD Bots Updates](https://t.me/XD_Botz)
"""
HELP_TXT = """
Nothing here
"""

START_BUTTONS = InlineKeyboardMarkup(
[[
InlineKeyboardButton("Source Code", url="https://github.com/saminsumesh/welcome-bot"),
InlineKeyboardButton("Support", url="https://t.me/xd_botzsupport")
]])

HELP_BUTTONS = InlineKeyboardMarkup(
[[
InlineKeyboardButton("Source Code", url="https://github.com/saminsumesh/welcome-bot"),
InlineKeyboardButton("Support", url="https://t.me/xd_botzsupport")
]])

ABOUT_BUTTONS = InlineKeyboardMarkup(
[[
InlineKeyboardButton("Source Code", url="https://github.com/saminsumesh/welcome-bot"),
InlineKeyboardButton("Support", url="https://t.me/xd_botzsupport")
]])

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
      await message.reply_text(
      text=START_TXT.format(message.from_user.mention),
      reply_markup=START_BUTTONS,
      disable_web_page_preview=True
      )
    
@Bot.on_message(filters.command(["help"]) & filters.private)
async def help(bot, message):
      await message.reply_text(
      text=HELP_TXT.format(message.from_user.mention),
      reply_markup=HELP_BUTTONS,
      disable_web_page_preview=True
      )

@Bot.on_message(filters.command(["about"]) & filters.private)
async def about(bot, message):
      await message.reply_text(
      text=ABOUT_TXT.format(message.from_user.mention),
      reply_markup=ABOUT_BUTTONS,
      disable_web_page_preview=True
     )
# This just an pyrogram welcome message bot that can be used in your groups.

@Bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(bot, message):
    message.reply_text(WELCOME_MESSAGE)
    
print("Bot is now running, If any issues contact us through @XD_Botzsupport")

Bot.run()
