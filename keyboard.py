from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="О нас"), KeyboardButton(text="О боте")],
    [KeyboardButton(text="Команды")]
],
    resize_keyboard=True,
    input_field_placeholder="Выбирите..",
    one_time_keyboard=True

)