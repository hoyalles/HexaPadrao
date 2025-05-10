from fastapi import FastAPI
from app.infrastructure.repositories import InMemoryUserRepository
from app.application.services import UserService
from app.interfaces.api import get_user_router

app = FastAPI()

repository = InMemoryUserRepository()
service = UserService(repository)
user_router = get_user_router(service)

app.include_router(user_router)