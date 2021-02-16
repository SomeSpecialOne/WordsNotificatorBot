from aiogram import executor

from loader import dp
import middlewares, filters, handlers


async def on_startup(dp):
    await notify_admin()


async def notify_admin():
    from loader import bot
    from data.config import admin
    await bot.send_message(chat_id=admin, text='Бот перезапущен!')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
