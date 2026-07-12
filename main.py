import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN
from keyboards.menu import main_menu


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):

    text = """
⚡ Привет, ты попал в главное меню Ze.Tech

Я занимаюсь сборкой ПК на заказ.

Доставка ПК осуществляется почти по всей территории РФ службами:

📦 CDEK
📮 Почта России
🛒 WB Track
🟣 Ozon Track
🔥 Avito доставка

Ознакомься с разделами ниже и отписывай мне!
"""

    await message.answer(
        text,
        reply_markup=main_menu()
    )


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
