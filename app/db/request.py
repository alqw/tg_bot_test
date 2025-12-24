from datetime import datetime
from calendar import monthrange
from app.db.models import async_session
from app.db.models import Expense
from sqlalchemy import select, and_, func


async def add(user_id, data):
    async with async_session() as session:
        session.add(
            Expense(
                user_id=user_id,
                sum=data["sum"],
                description=data["description"],
                date=datetime.now(),
            )
        )
        await session.commit()


async def getYears(user_id):
    async with async_session() as session:
        years = await session.scalars(
            select(func.strftime("%Y", Expense.date).label("year"))
            .where(Expense.user_id == user_id)
            .distinct()
            .order_by("year")
        )
        return years.all()


async def getAll(user_id, data):
    year = data["year"]
    month = data["month"]
    start_date = datetime(year, month, 1)
    last_day = monthrange(year, month)[1]
    end_date = datetime(year, month, last_day, 23, 59, 59)

    async with async_session() as session:
        expenses = await session.scalars(
            select(Expense).where(
                and_(
                    Expense.user_id == user_id,
                    Expense.date >= start_date,
                    Expense.date <= end_date,
                )
            )
        )
        return answer_expenses(expenses.all())


def answer_expenses(expenses):
    if not expenses:
        return "В этом месяце не было трат"

    sum = 0
    answer = []

    for exp in expenses:
        date = exp.date.strftime("%d.%m.%Y")
        answer.append(f"{date}\n{exp.sum}\n{exp.description}")
        sum += exp.sum

    answer.append("-----------")
    answer.append(f"Всего: {sum} тенге.")
    return "\n\n".join(answer)
