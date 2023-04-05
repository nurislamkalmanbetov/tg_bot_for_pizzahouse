from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from create_bot import TOKEN, dp, storage
from data_base import sqlite_db

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

from handlers.client import register_handlers_client  # импортируем функцию из client.py
from handlers.admin import register_handlers_admin
from handlers.other import register_handlers_other

register_handlers_client(dp)  # вызываем функцию для регистрации обработчиков
register_handlers_admin(dp)
register_handlers_other(dp)


async def on_startup(_):
    print('Бот запущен')
    sqlite_db.sql_start()

executor.start_polling(dp, on_startup=on_startup)
