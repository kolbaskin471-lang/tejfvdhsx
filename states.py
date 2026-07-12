from aiogram.fsm.state import StatesGroup, State


class OrderState(StatesGroup):

    city = State()
    contact = State()
