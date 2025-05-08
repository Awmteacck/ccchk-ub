ifrom telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("29691422")
API_HASH = input("7c2435a38e1c9f7417f62a5497db767a") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
