from aiogram.fsm.state import StatesGroup, State


class OrderState(StatesGroup):

    budget = State()

    purpose = State()

    city = State()
