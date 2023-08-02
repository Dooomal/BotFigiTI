# pip install -U --pre aiogram==3.0.0b6

import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_handlers
from config.config import Config, load_config

async def main():
    config: Config = load_config()
    token_b = config.tg_bot.token
    bot: Bot = Bot(token=token_b)
    dp: Dispatcher = Dispatcher()
    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())