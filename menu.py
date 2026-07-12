from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="⭐ Мои отзывы",
        url="https://t.me/ze_tech_FB"
    )

    kb.button(
        text="⚡ Мой ТГК",
        url="https://t.me/ze_tech_cfg"
    )

    kb.button(
        text="📜 Условия услуг",
        callback_data="rules"
    )

    kb.button(
        text="🎵 Мой TikTok",
        url="https://www.tiktok.com/@ze.tech.digital"
    )

    kb.button(
        text="🖥 Заказать сборку",
        url="https://t.me/pawawa420"
    )

    kb.adjust(1)

    return kb.as_markup()
