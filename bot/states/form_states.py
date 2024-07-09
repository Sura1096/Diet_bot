from aiogram.fsm.state import State, StatesGroup


class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_gender = State()
    fill_age = State()
    fill_weight = State()
    fill_height = State()
    fill_goal = State()
    fill_allergy = State()
    fill_sport = State()
    fill_job = State()
    fill_unwanted_products = State()
    fill_current_diet = State()
    fill_schedule = State()
    fill_bad_habits = State()
    fill_digestive_problems = State()
