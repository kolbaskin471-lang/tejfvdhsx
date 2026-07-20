import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN
from menu import main_menu

from handlers.rules import router as rules_router
from handlers.order import router as order_router

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

dp.include_router(rules_router)
dp.include_router(order_router)


@dp.message(CommandStart())
async def start(message: Message):

    text = """
⚡ Привет, ты попал в главное меню zetech

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
