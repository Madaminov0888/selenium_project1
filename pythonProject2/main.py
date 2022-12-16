import random
import time

from aiogram import types, executor, Dispatcher, Bot
import os
from parse import parse

TOKEN = "5940944119:AAGcF5yRmYP1AZmIImW66nn-HfqEfPO2aVk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

text = "✔️ Sanani Tekshirish (1 marta)"
text2 = "✔️ Yangilikka tekshirishni Boshlash"
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
keyboard.add(types.KeyboardButton(text=text),
             types.KeyboardButton(text=text2)
             )


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    if message.text == "/start":
        await message.answer(f"Assalomu aleykum {message.from_user.full_name}", reply_markup=keyboard)
        await message.answer("Malumot olish boshlandi...")

        async def parsing_control(attempt=0):
            if attempt == 20:
                await message.answer("Malumot Tekshirilmoqda...")
                await parsing_control(0)
            time.sleep(random.randint(40, 70))
            parse()
            await parsing_control(attempt + 1)

        await parsing_control()


executor.start_polling(dp, skip_updates=True)
