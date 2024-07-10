from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def gender_keyboard() -> InlineKeyboardBuilder:
    keyboard_builder = InlineKeyboardBuilder()
    category_buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Мужской',
                             callback_data='Мужской'),
        InlineKeyboardButton(text='Женский',
                             callback_data='Женский')
    ]

    keyboard_builder.row(*category_buttons)
    return keyboard_builder


async def save_keyboard() -> InlineKeyboardBuilder:
    keyboard_builder = InlineKeyboardBuilder()
    button: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Сохранить',
                             callback_data='сохранить')
    ]
    keyboard_builder.row(*button)
    return keyboard_builder
