from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from ..utils.unitofwork import MainUnitOfWork
from ..services.form_service import UsersService, FormService

from ..states.form_states import FSMFillForm
from ..filters.filters import check_name, check_age, check_weight, check_height
from ..lexicon.user_lexicon import LEXICON
from ..lexicon.form_lexicon import CANCEL_LEXICON, QUESTIONS_LEXICON, INCORRECT_DATA_LEXICON
from ..keyboards.keyboard_utils import gender_keyboard, save_keyboard


router = Router()


# Срабатывает на команду "/cancel" в любых состояниях, кроме состояния по умолчанию
@router.message(
    Command(commands='cancel'),
    ~StateFilter(default_state)
)
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=CANCEL_LEXICON['valid_cancel'])
    await state.clear()


# Срабатывает на команду "/cancel" в состоянии по умолчанию
@router.message(
    Command(commands='cancel'),
    StateFilter(default_state)
)
async def process_cancel_command(message: Message):
    await message.answer(text=CANCEL_LEXICON['invalid_cancel'])


# Срабатывает на команду /fillform и переводит бота в состояние ожидания ввода ФИО
@router.message(
    Command(commands='go'),
    StateFilter(default_state)
)
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text=QUESTIONS_LEXICON['name'])
    await state.set_state(FSMFillForm.fill_name)


# Срабатывает, если введено корректное ФИО и переводить в состояние ожидания ввода пола
@router.message(
    check_name,
    StateFilter(FSMFillForm.fill_name)
)
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    keyboard = await gender_keyboard()
    await message.answer(text=QUESTIONS_LEXICON['gender'], reply_markup=keyboard.as_markup())
    await state.set_state(FSMFillForm.fill_gender)


# Срабатывает, если ФИО будет введено некорректно
@router.message(StateFilter(FSMFillForm.fill_name))
async def warning_not_name(message: Message):
    await message.answer(text=INCORRECT_DATA_LEXICON['name'])


# Срабатывает, если введен корректный пол и переводит в состояние ожидания ввода возраста
@router.callback_query(F.data.in_(['Мужской', 'Женский']), StateFilter(FSMFillForm.fill_gender))
async def process_gender_sent(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(gender=callback.data)
    await callback.message.answer(text=QUESTIONS_LEXICON['age'])
    await state.set_state(FSMFillForm.fill_age)


# Срабатывает, если пол будет введен некорректно
@router.message(StateFilter(FSMFillForm.fill_gender))
async def warning_not_gender(message: Message):
    keyboard = await gender_keyboard()
    await message.answer(text=INCORRECT_DATA_LEXICON['gender'], reply_markup=keyboard.as_markup())


# Срабатывает, если введен корректный возраст и переводит в состояние ожидания ввода веса
@router.message(
    check_age,
    StateFilter(FSMFillForm.fill_age)
)
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(text=QUESTIONS_LEXICON['weight'])
    await state.set_state(FSMFillForm.fill_weight)


# Срабатывает, если возраст будет введен некорректно
@router.message(StateFilter(FSMFillForm.fill_age))
async def warning_not_age(message: Message):
    await message.answer(text=INCORRECT_DATA_LEXICON['age'])


# Срабатывает, если введен корректный вес и переводит в состояние ожидания ввода роста
@router.message(
    check_weight,
    StateFilter(FSMFillForm.fill_weight)
)
async def process_weight_sent(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer(text=QUESTIONS_LEXICON['height'])
    await state.set_state(FSMFillForm.fill_height)


# Срабатывает, если вес будет введен некорректно
@router.message(StateFilter(FSMFillForm.fill_weight))
async def warning_not_weight(message: Message):
    await message.answer(text=INCORRECT_DATA_LEXICON['weight'])


# Срабатывает, если введен корректный рост и переводит в состояние ожидания ввода цели
@router.message(
    check_height,
    StateFilter(FSMFillForm.fill_height)
)
async def process_height_sent(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await message.answer(text=QUESTIONS_LEXICON['goal'])
    await state.set_state(FSMFillForm.fill_goal)


# Срабатывает, если рост будет введен некорректно
@router.message(StateFilter(FSMFillForm.fill_height))
async def warning_not_height(message: Message):
    await message.answer(text=INCORRECT_DATA_LEXICON['height'])


# Срабатывает, если введена цель и переводит в состояние ожидания ввода аллергии на что-то
@router.message(StateFilter(FSMFillForm.fill_goal))
async def process_goal_sent(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(text=QUESTIONS_LEXICON['allergy'])
    await state.set_state(FSMFillForm.fill_allergy)


# Срабатывает, если введена аллергия и переводит в состояние ожидания ввода занятием спортом
@router.message(StateFilter(FSMFillForm.fill_allergy))
async def process_sport_sent(message: Message, state: FSMContext):
    await state.update_data(allergy=message.text)
    await message.answer(text=QUESTIONS_LEXICON['sport'])
    await state.set_state(FSMFillForm.fill_sport)


# Срабатывает, если введено занятие спортом и переводит в состояние ожидания ввода рабочего дня
@router.message(StateFilter(FSMFillForm.fill_sport))
async def process_activity_sent(message: Message, state: FSMContext):
    await state.update_data(sport=message.text)
    await message.answer(text=QUESTIONS_LEXICON['job'])
    await state.set_state(FSMFillForm.fill_job)


# Срабатывает, если введен рабочий день и переводит в состояние ожидания ввода нежелательных продуктов
@router.message(StateFilter(FSMFillForm.fill_job))
async def process_unwanted_products_sent(message: Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(text=QUESTIONS_LEXICON['unwanted_products'])
    await state.set_state(FSMFillForm.fill_unwanted_products)


# Срабатывает, если введены нежелательные продукты и переводит в состояние ожидания ввода текущего рациона питания
@router.message(StateFilter(FSMFillForm.fill_unwanted_products))
async def process_current_diet_sent(message: Message, state: FSMContext):
    await state.update_data(unwanted_products=message.text)
    await message.answer(text=QUESTIONS_LEXICON['current_diet'])
    await state.set_state(FSMFillForm.fill_current_diet)


# Срабатывает, если введен текущий рацион питания и переводит в состояние ожидания ввода рабочего графика
@router.message(StateFilter(FSMFillForm.fill_current_diet))
async def process_schedule_sent(message: Message, state: FSMContext):
    await state.update_data(current_diet=message.text)
    await message.answer(text=QUESTIONS_LEXICON['schedule'])
    await state.set_state(FSMFillForm.fill_schedule)


# Срабатывает, если введен рабочий график и переводит в состояние ожидания ввода вредных привычек
@router.message(StateFilter(FSMFillForm.fill_schedule))
async def process_bad_habits_sent(message: Message, state: FSMContext):
    await state.update_data(schedule=message.text)
    await message.answer(text=QUESTIONS_LEXICON['bad_habits'])
    await state.set_state(FSMFillForm.fill_bad_habits)


# Срабатывает, если введены вредные привычки и переводит в состояние ожидания ввода проблем с пищеварением
@router.message(StateFilter(FSMFillForm.fill_bad_habits))
async def process_digestive_problems_sent(message: Message, state: FSMContext):
    await state.update_data(bad_habits=message.text)
    await message.answer(text=QUESTIONS_LEXICON['digestive_problems'])
    await state.set_state(FSMFillForm.fill_digestive_problems)


# Срабатывает, если введены проблемы с пищеварением.
@router.message(StateFilter(FSMFillForm.fill_digestive_problems))
async def process_filled_form(message: Message, state: FSMContext):
    await state.update_data(digestive_problems=message.text)
    save_button = await save_keyboard()
    await message.answer(text=LEXICON['save_form'],
                         reply_markup=save_button.as_markup())


# Добавляет данные пользователя в БД.
@router.callback_query(F.data == 'сохранить')
async def process_save_button(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await state.clear()
    async with MainUnitOfWork() as uow:
        users_service = UsersService(uow)
        form_service = FormService(uow)
        user_id = await users_service.get_user_id(callback.from_user.id)
        if not user_id:
            await users_service.insert_user_id(callback.from_user.id)
            user_id = await users_service.get_user_id(callback.from_user.id)
            await form_service.insert_new_form(user_id, user_data)
        else:
            await form_service.update_form(user_id, user_data)
    await callback.message.answer(text=LEXICON['saved_form'])


# Срабатывает на остальные сообщения пользователя.
@router.message(StateFilter(default_state))
async def process_rest_messages(message: Message):
    await message.delete()
