import os
import logging
import asyncio

from tortoise import Tortoise
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.config import config
from src.routers import main_router
from src.middlewares import UserMessageMiddleware, UserCallbackQueryMiddleware
from src.utils.logging import setup_logging

logger = setup_logging(log_dir="logs", rotation="1 day", retention="31 days")

async def on_startup() -> None:
    await Tortoise.init(
        db_url=config.db_url.get_secret_value(),
        modules={"models": ["src.models.user"]}
    )
    
    await Tortoise.generate_schemas()
    
    logger.success("Bot succesfuly started.")

async def on_shutdown() -> None:
    await Tortoise.close_connections()
    
async def main() -> None:
    bot = Bot(config.bot_token.get_secret_value(),
                default=DefaultBotProperties(parse_mode=ParseMode.HTML)
            )
    
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    dp.message.middleware(UserMessageMiddleware())
    dp.callback_query.middleware(UserCallbackQueryMiddleware())
    
    dp.include_router(main_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped by keyboard interrupt or system exit.")
    except Exception as e:
        logger.exception(e)