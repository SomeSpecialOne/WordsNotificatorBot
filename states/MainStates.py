from aiogram.dispatcher.filters.state import StatesGroup, State


class Menu(StatesGroup):
    time_zone = State()  # start
    sleep_from = State()
    sleep_to = State()
    period = State()
    accept = State()

    done = State()
    stop = State()
