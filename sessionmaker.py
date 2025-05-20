from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = input("22658021")
API_HASH = input("6da533e7c45bc668182b5a0f5a4497dd") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
