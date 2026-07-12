from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from menu import main_menu


router = Router()


def back_button():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Назад",
        callback_data="back"
    )

    return kb.as_markup()


@router.callback_query(lambda c: c.data == "rules")
async def rules(callback: CallbackQuery):

    text = """
Условия услуг Ze.Tech

1. Осуществление гарантии

1.1. Причиной для возврата является только веская причина.
Не понравилось и подобное не является причиной.

1.2. Возврат товара может быть полным или частичным,
в зависимости от ситуации.


2. Гарантия

2.1. Гарантийный срок на Б/У комплектующие составляет 14 дней
с момента получения.

2.2. В течение 180 дней можно вернуть неработающее комплектующее
с полным возвратом средств или заменить его.

2.3. Если поломка произошла по вине заказчика,
возврат невозможен.


3. Оплата

3.1. Оплата ПК под заказ происходит полной предоплатой.

3.2. После оплаты отказ невозможен.

3.3. При покупке готового ПК возможна оплата при получении
через доставку Ozon.


4. Процесс сборки

4.1. Во время сборки специалист поддерживает связь
и уведомляет об изменениях.

4.2. Можно задавать любые вопросы по сборке.

4.3. После завершения сборки отправляются фотографии
готового ПК.


Оплачивая заказ, вы подтверждаете согласие
с данными условиями.
"""

    await callback.message.edit_text(
        text,
        reply_markup=back_button()
    )


@router.callback_query(lambda c: c.data == "back")
async def back(callback: CallbackQuery):

    await callback.message.edit_text(
        "Главное меню Ze.Tech",
        reply_markup=main_menu()
    )
