from aiogram import Router

from .user import router as user_router

routers: list[Router] = [
    user_router
]

main_router = Router()
main_router.include_routers(*routers)