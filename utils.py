import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import os


API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
if API_TOKEN is None:
    raise ValueError("Environment variable \"TELEGRAM_API_TOKEN\" \
            is not set, with no default")


ioloop = asyncio.get_event_loop()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, loop=ioloop, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

def auth(func):
    async def wrapper(message):
        #print(f"AUTH: {message}")
        if message["from"]["id"] not in {251538773}:
            print(message["from"]["id"])
            return await message.reply("Access denied", reply=False)

        return await func(message)
    return wrapper
