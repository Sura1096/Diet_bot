from aiogram import Bot
from aiogram.types import BotCommand
from ..lexicon.menu_commands_lexicon import MENU_LEXICON


async def set_menu_commands(bot: Bot) -> None:
    menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in MENU_LEXICON.items()
    ]

    await bot.set_my_commands(menu_commands)
