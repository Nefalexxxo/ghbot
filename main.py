
import openai
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Установите ваш токен от BotFather
BOT_TOKEN = '6468715758:AAExIc2gRQEJfOtQp6_fROj7AiLsttK5dsY'

# Установите ваш ключ API для OpenAI GPT
OPENAI_API_KEY = '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'

# Настройка бота и OpenAI GPT
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

# Настройка логгирования для Aiogram
logging.basicConfig(level=logging.INFO)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот, давай поговорим.")

# Обработка всех остальных сообщений
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def talk_to_gpt(message: types.Message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text,
            max_tokens=1000
        )
        bot_response = response.choices[0].text.strip()

        await message.answer(bot_response)

    except Exception as e:
        await message.answer("Произошла ошибка при обработке запроса.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)