from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column,sessionmaker, declarative_base
from sqlalchemy import String, Integer

from Config.config import DB_URL

engine = create_async_engine(DB_URL)

session_get = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class RegLog(Base):
    __tablename__ = "auto"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[int] = mapped_column(Integer, index=True)