# You can customise your welcome message while deploying this bot 
# All Copyright © goes to SaminSumesh
# GNU LICENSE V3 Under Public Source



import os
from pyrogram import Client, filters

Bot = Client(
"Simple Welcome Bot",
bot_token=os.environ.get("BOT_TOKEN"),
api_id=int(os.environ.get("API_ID")),
api_hash=os.environ.get("API_HASH")
)


GROUP = os.environ.get("")
WELCOME_MESSAGE = os.environ.get("")

# This just an pyrogram welcome message bot that can be used in your groups.

@Bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(bot, message):
    message.reply_text(WELCOM_MESSAGE)
    
print("Bot is now running, If any issues contact us through @XD_Botzsupport")

Bot.run()
