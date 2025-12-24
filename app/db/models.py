from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import Integer, BigInteger, String, DateTime
from datetime import datetime
import os

if not os.path.exists("data"):
    os.makedirs("data")

engine = create_async_engine(url="sqlite+aiosqlite:///data/db.sqlite")
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Expense(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    sum: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(255))
    date: Mapped[datetime] = mapped_column(DateTime)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
