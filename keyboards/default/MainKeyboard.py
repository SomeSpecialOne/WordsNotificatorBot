from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

settings_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Остановить рассылку 🚫')],
        [KeyboardButton(text='Изменить настройки ⚙')],
    ], resize_keyboard=True
)

hide = ReplyKeyboardRemove()
