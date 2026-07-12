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
от 100 до 150 тысяч
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

Теперь выберите назначение компьютера:
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

    orders[callback.from_user.id]["purpose"] = purpose

    await state.set_state(OrderState.city)

    await callback.message.edit_text(
        """
Отлично.

Теперь напишите ваш город.
        """
    )


@router.message(OrderState.city)
async def get_city(
    message: Message,
    state: FSMContext
):

    user_id = message.from_user.id

    orders[user_id]["city"] = message.text

    order = orders[user_id]


    username = message.from_user.username

    if username:
        telegram = f"@{username}"
    else:
        telegram = "Username отсутствует"


    admin_id = 7911808598


    await message.answer(
        """
Спасибо.

Ваша заявка отправлена специалисту Ze.Tech.

С вами свяжутся в ближайшее время.
        """
    )


    await message.bot.send_message(
        admin_id,
        f"""
Новый заказ Ze.Tech


Клиент:
{message.from_user.full_name}


Telegram:
{telegram}


Бюджет:
{order['budget']}


Назначение:
{order['purpose']}


Город:
{order['city']}
        """
    )


    await state.clear()
