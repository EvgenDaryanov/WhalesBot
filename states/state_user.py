from aiogram.fsm.state import State, StatesGroup


class StorageUsers(StatesGroup):
    get_amount = State()