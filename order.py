from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from states import OrderState


router = Router()

orders = {}


# Меню выбора бюджета

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


# Меню выбора назначения ПК

def purpose_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🎮 Игры",
        callback_data="purpose_games"
    )

    kb.button(
        text="🎬 Монтаж",
        callback_data="purpose_editing"
    )

    kb.button(
        text="💼 Работа",
        callback_data="purpose_work"
    )

    kb.button(
        text="🤖 3D / ИИ",
        callback_data="purpose_ai"
    )

    kb.adjust(1)

    return kb.as_markup()


# Кнопка "Заказать сборку"

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


# Выбор бюджета

@router.callback_query(lambda c: c.data.startswith("budget_"))
async def choose_budget(callback: CallbackQuery):

    budget_names = {

        "budget_50_100": "50-100 тыс ₽",
        "budget_100_150": "100-150 тыс ₽",
        "budget_150_250": "150-250 тыс ₽",
        "budget_250_plus": "250+ тыс ₽"

    }

    budget = budget_names.get(callback.data)

    orders[callback.from_user.id] = {
        "budget": budget
    }


    await callback.message.edit_text(
        f"""
Отлично 👍

Ваш бюджет:

💰 {budget}

Теперь расскажите:

🎯 Для чего нужен компьютер?
        """,
        reply_markup=purpose_menu()
    )


# Выбор назначения

@router.callback_query(lambda c: c.data.startswith("purpose_"))
async def choose_purpose(
    callback: CallbackQuery,
    state: FSMContext
):

    purpose_names = {

        "purpose_games": "🎮 Игры",
        "purpose_editing": "🎬 Монтаж",
        "purpose_work": "💼 Работа",
        "purpose_ai": "🤖 3D / ИИ"

    }


    purpose = purpose_names.get(callback.data)


    orders[callback.from_user.id]["purpose"] = purpose


    await state.set_state(OrderState.city)


    await callback.message.edit_text(
        f"""
Отлично 👍

Ваше назначение:

{purpose}

📍 Теперь напишите ваш город:
        """
    )


# Получение города

@router.message(OrderState.city)
async def get_city(
    message: Message,
    state: FSMContext
):

    user_id = message.from_user.id

    orders[user_id]["city"] = message.text


    await state.set_state(OrderState.contact)


    await message.answer(
        """
Отлично 👍

📞 Теперь отправьте ваш контакт:

- @username
- номер телефона
- ссылку на Telegram
        """
    )


# Получение контакта

@router.message(OrderState.contact)
async def get_contact(
    message: Message,
    state: FSMContext
):

    user_id = message.from_user.id

    orders[user_id]["contact"] = message.text


    order = orders[user_id]


    admin_id = 7911808598


    await message.answer(
        """
✅ Спасибо!

Ваша заявка отправлена специалисту Ze.Tech ⚡

С вами свяжутся в ближайшее время.
        """
    )


    await message.bot.send_message(

        admin_id,

        f"""
🔥 Новый заказ Ze.Tech


👤 Клиент:

{message.from_user.full_name}


💰 Бюджет:

{order['budget']}


🎯 Назначение:

{order['purpose']}


📍 Город:

{order['city']}


📞 Контакт:

{order['contact']}


Telegram:

@{message.from_user.username}
"""

    )


    await state.clear()
