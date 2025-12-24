from aiogram import Bot, Dispatcher
import dotenv
import os
from app.router import router
from app.db.models import async_main

dotenv.load_dotenv()


async def start_bot():
    await async_main()
    bot = Bot(token=os.getenv("TELEGRAM_API_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
