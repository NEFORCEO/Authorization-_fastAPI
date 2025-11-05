from typing import Annotated

from fastapi import Depends
from database.db import engine, Base, AsyncSession, session_get


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def get_sess() -> AsyncSession:
    async with session_get() as session:
        yield session
        
SessionDep = Annotated[AsyncSession, Depends(get_sess)]
    