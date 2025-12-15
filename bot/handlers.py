from aiogram import types
from aiogram.filters import Command

from jobs.search import search_jobs
from llm.cover_letter import generate_cover_letter
from bot.keyboards import job_keyboard
from db.db import save_application

current_jobs = []

def register_handlers(dp):

    @dp.message(Command("start"))
    async def start(msg: types.Message):
        await msg.answer(
            "Hi! I can help you find Junior Python Developer jobs in the UK.\n"
            "Use /search to begin."
        )

    @dp.message(Command("search"))
    async def search(msg: types.Message):
        global current_jobs
        current_jobs = search_jobs()


        if not current_jobs:
            await msg.answer("No jobs found.")
            return

        job = current_jobs[0]
        await msg.answer(
            f"📌 {job['title']}\n"
            f"🏢 {job['company']}\n"
            f"🔗 {job['url']}",
            reply_markup=job_keyboard()
        )

    @dp.message(Command("cover"))
    async def cover(msg: types.Message):
        if not current_jobs:
            await msg.answer("Use /search first.")
            return

        job = current_jobs[0]
        letter = generate_cover_letter(job)
        await msg.answer(letter)

    @dp.message(Command("applied"))
    async def applied(msg: types.Message):
        if not current_jobs:
            await msg.answer("Nothing to mark.")
            return

        job = current_jobs[0]
        save_application(job)
        await msg.answer("✅ Marked as applied.")
