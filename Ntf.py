import asyncio

from NotificatorClass import Notificator


async def start(period: int):
    x = Notificator(period)
    await x.start()


loop = asyncio.get_event_loop()
tasks = [loop.create_task(start(period)) for period in [3600, 7200, 10800]]
wait_tasks = asyncio.wait(tasks)


if __name__ == '__main__':
    loop.run_until_complete(wait_tasks)
