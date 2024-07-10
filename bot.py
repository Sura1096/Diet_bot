import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from bot.config.config import load_config
from bot.handlers import commands_handlers, form_handlers
from bot.keyboards.set_menu import set_menu_commands


async def main() -> None:
    config = load_config()
    bot_token = config.tg_bot.GET_BOT_TOKEN
    bot = Bot(token=bot_token)

    # Для хранения данных состояний всех пользователей во время работы FSM
    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)
    dp = Dispatcher(storage=storage)
    await set_menu_commands(bot)

    dp.include_router(commands_handlers.router)
    dp.include_router(form_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
