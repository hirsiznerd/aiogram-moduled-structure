from typing import Callable, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from src.models import User

class UserMessageMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, dict[str, any]], Awaitable[Any]],
                       event: Message,
                       data: dict[str, Any]
                       ):
        
        user = await User.get_or_create(id=event.from_user.id)
        data["user"] = user[0]
        
        return await handler(event, data)
    
class UserCallbackQueryMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[CallbackQuery, dict[str, any]], Awaitable[Any]],
                       event: CallbackQuery,
                       data: dict[str, Any]
                       ):
        
        user = await User.get_or_create(id=event.from_user.id)
        data["user"] = user[0]
        
        return await handler(event, data)