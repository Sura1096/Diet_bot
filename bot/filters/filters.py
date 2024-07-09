from aiogram.types import Message


def check_name(message: Message):
    text = message.text.replace(' ', '')
    return text.isalpha()


def check_age(message: Message):
    return (message.text.startswith('Возраст') and
            (message.text.endswith('лет') or message.text.endswith('года')))


def check_weight(message: Message):
    return message.text.startswith('Вес') and message.text.endswith('кг')


def check_height(message: Message):
    return message.text.startswith('Рост') and message.text.endswith('см')
