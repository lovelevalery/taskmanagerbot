from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import dateparser
import datetime
from utils import dp, auth
from config import *

async def periodic(sleep_for):
    while True:
        await match_time((13, 47))
        now = datetime.utcnow()
        for id in {251538773}:
            await bot.send_message(id, f"{now}",
                                   disable_notification=True)