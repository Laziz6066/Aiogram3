from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.database.requests as rq


router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply("Добро пожаловать в магазин кроссовок.", reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выбкрите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def item(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}'
                                  f'\nЦена: {item_data.price}$')


# @router.message(Command('help'))
# async def get_help(message: Message):
#     await message.answer('Это команда /help')


# @router.message(F.text == 'kak dela?')
# async def how_are_you(message: Message):
#     await message.answer('OK')
#
#
# @router.message(Command('get_photo'))
# async def get_photo(message: Message):
#     await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id="
#                                      "884edb525425300d10ba53dd8b1ee02e1d"
#                                      "383cda-4079679-images-thumbs&n=13.png", caption='Yandex')
#
#
# @router.message(F.photo)
# async def get_photo(message: Message):
#     await message.answer(f'ID photo: {message.photo[-1].file_id}')
#
#
# @router.callback_query(F.data == 'catalog')
# async def catalog(callback: CallbackQuery):
#     await callback.answer('Вы выбрали каталог')
#     await callback.message.edit_text('Привет', reply_markup=await kb.inline_cars())
#
#
# @router.message(Command('reg'))
# async def reg_one(message: Message, state: FSMContext):
#     await state.set_state(Reg.name)
#     await message.answer('Введите своё имя:')
#
#
# @router.message(Reg.name)
# async def reg_two(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Reg.number)
#     await message.answer('Введите номер телефона: ')
#
#
# @router.message(Reg.number)
# async def reg_three(message: Message, state: FSMContext):
#     await state.update_data(number=message.text)
#     data = await state.get_data()
#     await message.answer(f'Спасибо, регистрация завршена\nИмя: {data["name"]}\nНомер: {data["number"]}')
#     await state.clear()