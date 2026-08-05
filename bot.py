import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🤖 Добро пожаловать в AI Studio!\n\n"
        "Пока это первая версия бота.\n\n"
        "Следующий этап — красивое меню."
    )


@dp.message()
async def echo(message: Message):
    await message.answer(
        f"Вы написали:\n\n{message.text}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())