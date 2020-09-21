import os
import asyncio

from aiogram import Bot, Dispatcher, executor, types
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
if API_TOKEN == None:
	raise ValueError("Environment variable \"TELEGRAM_API_TOKEN\" is not set, with no default")


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def auth(func):
	async def wrapper(message):
		if message["from"]["id"] not in {251538773}:
			print(message["from"]["id"])
			return await message.reply("Access denied", reply=False)

		return await func(message)
	return wrapper


		
@dp.message_handler(commands=["start", "help"])
@auth
async def send_welcome(msg: types.Message):
	await message.reply(
			"Бот для трекинга задач",
			"Добавить задачу: /new",
			 "Посмотреть на список всех задач: /all",
			  reply=False)


@dp.message_handler()
@auth
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

	
if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
