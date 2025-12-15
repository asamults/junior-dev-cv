from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def job_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="/cover"),
            KeyboardButton(text="/applied")
        ]],
        resize_keyboard=True
    )
