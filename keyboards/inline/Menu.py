from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.Callbackdatas import menu_callback

time_zone = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='-2', callback_data=menu_callback.new(item_name='-2')),
            InlineKeyboardButton(text='-1', callback_data=menu_callback.new(item_name='-1')),
            InlineKeyboardButton(text='+0', callback_data=menu_callback.new(item_name='0')),
            InlineKeyboardButton(text='+1', callback_data=menu_callback.new(item_name='1')),
            InlineKeyboardButton(text='+2', callback_data=menu_callback.new(item_name='2')),
            InlineKeyboardButton(text='+3', callback_data=menu_callback.new(item_name='3')),
            InlineKeyboardButton(text='+4', callback_data=menu_callback.new(item_name='4'))
        ]
    ]
)

sleep_from = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='21:00', callback_data=menu_callback.new(item_name='21')),
            InlineKeyboardButton(text='22:00', callback_data=menu_callback.new(item_name='22'))
        ],
        [
            InlineKeyboardButton(text='23:00', callback_data=menu_callback.new(item_name='23')),
            InlineKeyboardButton(text='00:00', callback_data=menu_callback.new(item_name='0'))
        ]
    ]
)

sleep_to = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='06:00', callback_data=menu_callback.new(item_name='6')),
            InlineKeyboardButton(text='07:00', callback_data=menu_callback.new(item_name='7'))
        ],
        [
            InlineKeyboardButton(text='08:00', callback_data=menu_callback.new(item_name='8')),
            InlineKeyboardButton(text='09:00', callback_data=menu_callback.new(item_name='9'))
        ]
    ]
)

period = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='час', callback_data=menu_callback.new(item_name='3600')),
            InlineKeyboardButton(text='два часа', callback_data=menu_callback.new(item_name='7200'))
        ],
        [
            InlineKeyboardButton(text='три часа', callback_data=menu_callback.new(item_name='10800'))
        ]
    ]
)

accept = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Да ✅', callback_data=menu_callback.new(item_name='yes')),
            InlineKeyboardButton(text='Нет ❌', callback_data=menu_callback.new(item_name='no'))
        ]
    ]
)

sending_on = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Возобновить рассылку ✅', callback_data=menu_callback.new(item_name='send'))
        ]
    ]
)
