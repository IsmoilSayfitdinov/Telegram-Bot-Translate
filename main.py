import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from translate import Translator
import keyboard as kb


BOT_TOKEN = "7161407802:AAHWlNHghE_OVFuIy7tIliBy89uF9MfAgPQ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


ru_len = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".lower()
eng_lan = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
uz_lan = "'abdefghijklmnopqrstuvxyzoʻgʻchshyuyayo".lower()


@dp.message(F.text == "О боте")
async def about_bot(message: types.Message):
    await message.reply("Bot Name: Tarnslate\nCreate Date: 18.03.2024\nCreate Language: Python\n Create Libiry: Aiogram 3", reply_markup=kb.keyboard)

@dp.message(F.text == "О нас")
async def about_me(message: types.Message):
    await message.reply("Owner: Ismoil Sayfitdinov")

@dp.message(Command("logo"))
async def get_logo(message: types.Message):
    await message.answer_photo("https://play-lh.googleusercontent.com/yzRPpY6Klkd8vn9ZBDhZ2U_6xSjK7-kKe4dDHMGIiwRvI6WJrKSlsmsInXupLzntgKDZ")


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет я переводчик \n Hi I am Translate \n Enter text ->",
                         reply_markup=kb.keyboard)

@dp.message(F.text == "Команды")
async def command(message: types.Message):
    await message.reply("/start \n /help  \n /logo")
@dp.message()
async def message_echo(message: types.Message):
    text = message.text
    if text[0].lower() in ru_len:
        translator = Translator(from_lang="ru", to_lang="eng")
    elif text[0].lower() in uz_lan:
        translator = Translator(from_lang="uz", to_lang='ru')
    elif text[0].lower() not in eng_lan:
        translator = Translator(from_lang="en", to_lang="ru")
    else:
        await message.answer("Please Enter Russian or English language !")
        return
    translation = translator.translate(text)
    await message.answer(translation)



async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
