from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import default_state
from ..lexicon.user_lexicon import LEXICON


router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])
