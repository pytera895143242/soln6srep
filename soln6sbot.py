from aiogram import executor
from misc import dp
import asyncio
import handlers
from handlers.commands_start import posting

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(posting())
    executor.start_polling(dp, skip_updates=True)