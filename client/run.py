from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.models.model import init_db

@asynccontextmanager
async def start_app(app: FastAPI):
    print("Программа запущена")
    await init_db()
    yield
    print("Программа завершила свою работу")