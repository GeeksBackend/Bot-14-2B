from aiogram import Bot, Dispatcher, types, executor
from config import token
import logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_keyboard = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Заявка на курсы')
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboard)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    print(message)
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=start_button)

@dp.message_handler(text='О нас')
async def about_us(message:types.Message):
    await message.reply("Geeks - это айти курсы в Бишкеке, Кара-Балте, Оше и в Ташкенте!")

@dp.message_handler(text="Адрес")
async def send_address(message:types.Message):
    await message.answer("Наш адрес: Мырзалы Аматова 1Б (БЦ Томирис)")
    await message.answer_location(40.51936, 72.8027)

courses_keyboards = [
    types.KeyboardButton('Backend'),
    types.KeyboardButton('Frontend'),
    types.KeyboardButton('Android'),
    types.KeyboardButton('iOS'),
    types.KeyboardButton('UX/UI'),
    types.KeyboardButton('Назад'),
]
courses_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_keyboards)

@dp.message_handler(text="Курсы")
async def send_courses(message:types.Message):
    await message.answer("Вот наши курсы:", reply_markup=courses_button)

@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.reply("Backend - это внутреняя часть сайта или приложения.\nСрок обучения 5 месяцев\nСтоимость: 10000 KGS в месяц")

@dp.message_handler(text="Назад")
async def backroll(message:types.Message):
    await start(message)

executor.start_polling(dp)