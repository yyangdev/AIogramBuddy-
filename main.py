import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot: Bot = Bot(token=BOT_TOKEN)  
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
    text = '''👋 Привет! Я твой первый учебный бот на aiogram!
Используй команду /help, чтобы увидеть что я умею.'''

    await message.answer(text)

@dp.message(Command('help'))
async def help(message: Message):
    text = """📋 Список доступных команд:
/start - Начальное приветствие
/help - Показать эту справку
/about - Информация о боте и разработчике
/links - Полезные ссылки для обучения"""

    await message.answer(text)

@dp.message(Command('about'))
async def about(message: Message):
    text = """ℹ️ **Обо мне:**
Меня зовут InfoHelper.
Я создан как учебный проект для освоения библиотеки aiogram.
Мой разработчик: [@yangspays].
Цель: помочь сделать первые шаги в создании Telegram-ботов."""

    await message.answer(text)
@dp.message(Command('links'))
async def links(message: Message):
    text = '''🔗 **Полезные ресурсы:**
• Документация aiogram: https://docs.aiogram.dev/
• Официальная документация Telegram Bot API: https://core.telegram.org/bots/api
• Учебник для начинающих: https://mastergroosha.github.io/aiogram-3-guide/
Удачи в обучении! 💻'''
    await message.answer(text)

@dp.message(F.text)
async def gov(message: Message):
    text = '''🤔 Я пока понимаю только команды.
Введите /help для получения списка доступных команд.'''
    await message.answer(text)

async def main():
    print("✅ Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())