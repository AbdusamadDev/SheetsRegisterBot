from aiogram.dispatcher.filters.state import State, StatesGroup

class UserDetails(StatesGroup):
    fullname = State()
    phone = State()
    region = State()
    identified_from = State()
