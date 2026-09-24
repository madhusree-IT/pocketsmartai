from fastapi import APIRouter
from pydantic import BaseModel
import aiosqlite

router = APIRouter()

DATABASE = "pocketsmart.db"


class Expense(BaseModel):
    category: str
    amount: float
    description: str = ""


@router.post("/expenses")
async def add_expense(expense: Expense):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(
            "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
            (expense.category, expense.amount, expense.description)
        )
        await db.commit()

    return {"message": "Expense added successfully"}


@router.get("/expenses")
async def get_expenses():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute(
            "SELECT id, category, amount, description FROM expenses"
        )
        rows = await cursor.fetchall()

    return {"expenses": rows}


@router.get("/budget")
async def get_budget():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute("SELECT SUM(amount) FROM expenses")
        row = await cursor.fetchone()

    total = row[0] or 0

    return {
        "total_spending": total,
        "currency": "INR"
    }


@router.get("/recommendations")
async def recommendations():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute("SELECT SUM(amount) FROM expenses")
        row = await cursor.fetchone()

    total = row[0] or 0

    if total > 10000:
        message = "Consider reducing unnecessary spending."
    elif total > 5000:
        message = "Your spending is moderate. Try increasing savings."
    else:
        message = "Your spending is within a reasonable range."

    return {"recommendation": message}