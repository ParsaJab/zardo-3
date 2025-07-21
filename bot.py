import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

users = {}

@dp.message(Command("start"))
async def start_handler(message: Message):
    uid = message.from_user.id
    if uid not in users:
        users[uid] = {"gold": 0, "clicks": 0}
    await message.answer("🤑 Welcome to ZARDO!\nUse /click to earn Gold\nUse /profile to view your stats.")

@dp.message(Command("click"))
async def click_handler(message: Message):
    uid = message.from_user.id
    users[uid]["gold"] += 3
    users[uid]["clicks"] += 1
    await message.answer(f"💰 You earned 3 Gold!\nTotal Gold: {users[uid]['gold']}")

@dp.message(Command("profile"))
async def profile_handler(message: Message):
    uid = message.from_user.id
    user = users.get(uid, {"gold": 0, "clicks": 0})
    await message.answer(f"👤 Your Stats:\nGold: {user['gold']}\nClicks: {user['clicks']}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
