from loguru import logger
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.models import User, UserPydanticModel

router = Router(name="user")

@router.message(Command("start"))
async def start_command(message: Message, user: User):
    logger.info("Start command executed.\n"
                f"User from database: {UserPydanticModel.model_validate(user).model_dump_json(indent=4)}")
    await message.reply("Hello, world!")