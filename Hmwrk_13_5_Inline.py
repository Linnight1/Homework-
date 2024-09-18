import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.row(button, button2)

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb_2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button4 = InlineKeyboardButton(text="Формулы расчета", callback_data='formulas')
kb_2.row(button3, button4)
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
@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст")
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
    await message.answer(f"Ваша норма калорий: {float(data['third']) * 10 + 6.25 * float(data['second']) - 5 * float(data['first']) - 161}")
    await state.finish()
@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_2)
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)