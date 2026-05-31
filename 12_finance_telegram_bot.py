import logging
import sqlite3
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ================= settings =================
TOKEN = "PASTE_YOUR_TOKEN_HERE"  # <-- token from  BotFather
DB_NAME = "finance.db"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# ================= Data base =================
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    amount INTEGER,
    date TEXT
)
""")
conn.commit()

# ================= buttons =================
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.row(
    KeyboardButton("➕ Add money spend"),
    KeyboardButton("📅 Today")
)
main_kb.row(
    KeyboardButton("📊 Statistics")
)

# ================= /start =================
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "💰 Financial helper\n\n"
        "Use buttons 👇",
        reply_markup=main_kb
    )

# ================= Spend add =================
@dp.message_handler(text="➕ Add a spend")
async def add_expense_start(message: types.Message):
    await message.answer(
        "✏️ ВвеAdd a spend in format:\n\n"
        "coffee 3"
    )

@dp.message_handler(lambda message: len(message.text.split()) == 2)
async def add_expense_finish(message: types.Message):
    title, amount = message.text.split()

    if not amount.isdigit():
        return

    cursor.execute(
        "INSERT INTO expenses (user_id, title, amount, date) VALUES (?, ?, ?, ?)",
        (
            message.from_user.id,
            title,
            int(amount),
            datetime.now().strftime("%Y-%m-%d")
        )
    )
    conn.commit()

    await message.answer(
        f"✅ Added: {title} — {amount} ₽",
        reply_markup=main_kb
    )

# ================= today =================
@dp.message_handler(text="📅 Today")
async def today_stats(message: types.Message):
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "SELECT title, amount FROM expenses WHERE user_id = ? AND date = ?",
        (message.from_user.id, today)
    )
    rows = cursor.fetchall()

    if not rows:
        await message.answer("No spend today 👍", reply_markup=main_kb)
        return

    total = 0
    text = "📅 Today's spend:\n\n"
    for title, amount in rows:
        text += f"• {title}: {amount} ₽\n"
        total += amount

    text += f"\n💸 Total: {total} ₽"
    await message.answer(text, reply_markup=main_kb)

# ================= Statistics =================
@dp.message_handler(text="📊 Statistics")
async def all_stats(message: types.Message):
    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE user_id = ?",
        (message.from_user.id,)
    )
    total = cursor.fetchone()[0]
    total = total if total else 0

    await message.answer(
        f"💰 Total spend: {total} ₽",
        reply_markup=main_kb
    )

# ================= Run =================
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
