from handlers import get_handler  # Импортируем функцию напрямую
import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(get_handler())  # Здесь вызываем функцию корректно
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())