import random
from aiogram import types
from create import dp



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message): 
    await message.answer('Привет тебе')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Я ничего не умею')

@dp.message_handler()
async def mes_all(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, смотри, что я поймал - {message.text}')

