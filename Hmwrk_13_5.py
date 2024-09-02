import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.row(button, button2)

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)
@dp.message_handler(text=["Информация"])
async def info(message):
    await message.answer("Информация")
@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст")
    await UserState.age.set()
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    await message.answer(float(data['third']) * 10 + 6.25 * float(data['second']) - 5 * float(data['first']) - 161)
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)