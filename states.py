from aiogram.dispatcher.filters.state import State, StatesGroup

class UserDetails(StatesGroup):
    fullname = State()
    course = State()
    phone = State()
    optional_phone = State()
    region = State()
    strict = State()
    exam_date = State()
    identified_from = State()
