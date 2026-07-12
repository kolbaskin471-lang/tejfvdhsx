from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


def budget_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="💵 50-100 тыс ₽",
        callback_data="budget_50_100"
    )

    kb.button(
        text="💵 100-150 тыс ₽",
        callback_data="budget_100_150"
    )

    kb.button(
        text="💵 150-250 тыс ₽",
        callback_data="budget_150_250"
    )

    kb.button(
        text="💵 250+ тыс ₽",
        callback_data="budget_250_plus"
    )

    kb.adjust(1)

    return kb.as_markup()


@router.callback_query(lambda c: c.data == "order")
async def start_order(callback: CallbackQuery):

    await callback.message.edit_text(
        """
🖥 Заказ сборки Ze.Tech

Начнём подбор вашего ПК.

💰 Укажите ваш бюджет:
        """,
        reply_markup=budget_menu()
    )
