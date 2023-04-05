from aiogram import types, Dispatcher
from create_bot import dp
import json, string

# загружаем файл JSON один раз и сохраняем его содержимое в переменной
with open('cenz.json', 'r', encoding='utf-8') as f:
    censored_words = set(json.load(f))


# @dp.message_handler() # фильтр для матов
async def echo_send(message : types.Message):
    words = {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}
    if words.intersection(censored_words):
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
