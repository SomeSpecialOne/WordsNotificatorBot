from aiogram import types
# from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from states.MainStates import Menu
from ClientClass import User
from keyboards.inline.Menu import time_zone, sleep_from, sleep_to, period, accept, sending_on
from keyboards.inline.Callbackdatas import menu_callback
from keyboards.default.MainKeyboard import settings_kb, hide

from loader import dp, db


def get_users(database=db):
    global users
    sql = database.cursor()
    sql.execute('''SELECT [User_id], [First_name], [Last_name], [Username], 
                    [Time_zone], [Sleep_from], [Sleep_to], [Period] FROM Users''')
    ans = sql.fetchall()
    for data in ans:
        user = User(data[0], data[1], data[2], data[3])
        user.time_zone = data[4]
        user.sleep_from = data[5]
        user.sleep_to = data[6]
        user.period = data[7]
        users.update({data[0]: user})


users = {}


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    global users

    await message.answer('👋')
    await message.answer(f"Привет, {message.from_user.first_name}\n"
                         f"Я помогу тебе выучить новые слова на английском!"
                         f"Для этого тебе нужно пройти небольшую настройку...")

    user = User(message.from_user.id, message.from_user.first_name,
                message.from_user.last_name, message.from_user.username)
    user.create_user()

    users.update({message.from_user.id: user})

    await message.answer('Мне нужно знать твой часовой пояс UTC 🌍\n'
                         'Москва, Донецк, Белгород +3, Киев +2 и т.д.', reply_markup=time_zone)

    await Menu.time_zone.set()


@dp.callback_query_handler(state=Menu.time_zone)
async def get_answer(call: types.CallbackQuery):
    global users
    if call.data == 'decision:-2':
        utc = -2
    elif call.data == 'decision:-1':
        utc = -1
    elif call.data == 'decision:0':
        utc = 0
    elif call.data == 'decision:1':
        utc = 1
    elif call.data == 'decision:2':
        utc = 2
    elif call.data == 'decision:3':
        utc = 3
    else:
        utc = 4
    try:
        user = users[call.from_user.id]
    except KeyError:
        get_users()
        user = users[call.from_user.id]

    await call.message.edit_text('Теперь нужно определить время, в которое я не буду тебя беспокоить\n'
                                 'В каком часу ты ложишься спать?🌙', reply_markup=sleep_from)

    user.update_time_zone(utc)
    users.update({call.from_user.id: user})
    await Menu.sleep_from.set()


@dp.callback_query_handler(state=Menu.sleep_from)
async def get_answer(call: types.CallbackQuery):
    global users
    if call.data == 'decision:21':
        time_sleep_from = 21
    elif call.data == 'decision:22':
        time_sleep_from = 22
    elif call.data == 'decision:23':
        time_sleep_from = 23
    else:
        time_sleep_from = 0
    try:
        user = users[call.from_user.id]
    except KeyError:
        get_users()
        user = users[call.from_user.id]

    await call.message.edit_text('А в каком часу встаешь?⏰', reply_markup=sleep_to)

    user.update_time_sleep_from(time_sleep_from)
    users.update({call.from_user.id: user})
    await Menu.sleep_to.set()


@dp.callback_query_handler(state=Menu.sleep_to)
async def get_answer(call: types.CallbackQuery):
    global users
    if call.data == 'decision:6':
        time_sleep_to = 6
    elif call.data == 'decision:7':
        time_sleep_to = 7
    elif call.data == 'decision:8':
        time_sleep_to = 8
    else:
        time_sleep_to = 9
    try:
        user = users[call.from_user.id]
    except KeyError:
        get_users()
        user = users[call.from_user.id]

    await call.message.edit_text('Ну и последний этап.\n'
                                 'Как часто тебе присылать слова?⏱\n'
                                 'Раз в ...', reply_markup=period)

    user.update_time_sleep_to(time_sleep_to)
    users.update({call.from_user.id: user})
    await Menu.period.set()


@dp.callback_query_handler(state=Menu.period)
async def get_answer(call: types.CallbackQuery):
    global users
    if call.data == 'decision:3600':
        period_f = 3600
    elif call.data == 'decision:7200':
        period_f = 7200
    else:
        period_f = 10800
    try:
        user = users[call.from_user.id]
    except KeyError:
        get_users()
        user = users[call.from_user.id]

    user.update_period(period_f)
    current_time = user.get_current_time()
    msg = f'Так, на часах у тебя сейчас {current_time},\n' \
          f'Не беспокоить тебя с {user.sleep_from}:00 до {user.sleep_to}:00\n'
    if user.period == 3600:
        msg += f'И присылать тебе новое слово каждый час.\n' \
               f'Все правильно?'
    elif user.period == 7200:
        msg += f'И присылать тебе новое слово каждые два часа.\n' \
               f'Все правильно?'
    else:
        msg += f'И присылать тебе новое слово каждые три часа.\n' \
               f'Все правильно?'
    await call.message.edit_text(text=msg, reply_markup=accept)
    users.update({call.from_user.id: user})
    await Menu.accept.set()


@dp.callback_query_handler(state=Menu.accept)
async def get_answer(call: types.CallbackQuery):
    global users
    if call.data == 'decision:yes':
        try:
            user = users[call.from_user.id]
        except KeyError:
            get_users()
            user = users[call.from_user.id]
        time_to_send = user.get_time_to_send()
        user.save_settings()
        await call.message.edit_text('Отлично. Начинаем!')
        await call.message.answer(f'Я пришлю тебе первое слово в {time_to_send}', reply_markup=settings_kb)
        await Menu.done.set()
    elif call.data == 'decision:no':
        await call.message.edit_text('Давай снова настроим все.\n'
                                     'Выбери свой часовой пояс UTC', reply_markup=time_zone)
        await Menu.time_zone.set()


@dp.message_handler(text='Изменить настройки ⚙', state="*")
async def get_answer(message: types.Message):
    try:
        user = users[message.from_user.id]
    except KeyError:
        get_users()
        try:
            user = users[message.from_user.id]
        except KeyError:
            await message.answer('Нажми /start')
            return
    await message.answer('Выбери свой часовой пояс UTC', reply_markup=time_zone)
    await Menu.time_zone.set()


@dp.message_handler(text='Остановить рассылку 🚫', state="*")
async def get_answer(message: types.Message):
    global users
    try:
        user = users[message.from_user.id]
    except KeyError:
        get_users()
        try:
            user = users[message.from_user.id]
        except KeyError:
            await message.answer('Нажми /start')
            return
    user.off_on(0)
    await message.answer('😔', reply_markup=hide)
    await message.answer('Рассылка остановлена', reply_markup=sending_on)
    await Menu.stop.set()


@dp.callback_query_handler(menu_callback.filter(item_name='send'), state=Menu.stop)
async def get_answer(call: types.CallbackQuery):
    global users
    try:
        user = users[call.from_user.id]
    except KeyError:
        get_users()
        user = users[call.from_user.id]
    user.off_on(1)
    time_to_send = user.get_time_to_send()
    await call.message.edit_text('👍')
    await call.message.answer(f'Я пришлю тебе первое слово в {time_to_send}', reply_markup=settings_kb)
    await Menu.done.set()


@dp.message_handler(state='*')
async def answer_other(message: types.Message):
    await message.answer('😕')


# @dp.message_handler(content_types=['sticker'])
# async def sticker(message: types.Message):
#     print(message.sticker.file_id)
