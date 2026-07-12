from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from states import OrderState


router = Router()

orders = {}


def purpose_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Игры",
        callback_data="purpose_games"
    )

    kb.button(
        text="Монтаж",
        callback_data="purpose_editing"
    )

    kb.button(
        text="Работа",
        callback_data="purpose_work"
    )

    kb.button(
        text="3D / ИИ",
        callback_data="purpose_ai"
    )

    kb.adjust(1)

    return kb.as_markup()


@router.callback_query(lambda c: c.data == "order")
async def start_order(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.set_state(OrderState.budget)

    await callback.message.edit_text(
        """
Заказ сборки Ze.Tech

Напишите ваш бюджет на ПК.

Пример:
150000

или

100-150 тысяч
        """
    )


@router.message(OrderState.budget)
async def get_budget(
    message: Message,
    state: FSMContext
):

    orders[message.from_user.id] = {
        "budget": message.text
    }

    await state.set_state(OrderState.purpose)

    await message.answer(
        """
Отлично.

Выберите назначение компьютера:
        """,
        reply_markup=purpose_menu()
    )


@router.callback_query(lambda c: c.data.startswith("purpose_"))
async def choose_purpose(
    callback: CallbackQuery,
    state: FSMContext
):

    purpose_names = {
        "purpose_games": "Игры",
        "purpose_editing": "Монтаж",
        "purpose_work": "Работа",
        "purpose_ai": "3D / ИИ"
    }

    purpose = purpose_names.get(callback.data)

    orders[
