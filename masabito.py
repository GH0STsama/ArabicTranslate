from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.tl.custom import Message
from googletrans import Translator
from os import getenv

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("MASABITO_BOT")

bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token = BOT_TOKEN)

async def translator(trans: str) -> str:
    tr = Translator()
    cont = 0
    while cont < 10:
        try: return tr.translate(trans, dest = "ar").text
        except: cont += 1
    return trans

@bot.on(NewMessage())
async def messages_handler(event: Message):
    if event.raw_text: 
        await event.reply(await translator(event.raw_text))
    else: 
        await event.reply("✖️ Dame un texto para traducir")

print("Masabito Iniciado")
bot.run_until_disconnected()