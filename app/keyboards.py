from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.database.requests import get_categories, get_category_item
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
    ], resize_keyboard=True, input_field_placeholder='Select a menu item.')


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


# main = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
#     [InlineKeyboardButton(text='Корзина', callback_data='basket')],
#     [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
# ])
#
# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Youtube, TiTa', url='https://www.youtube.com/@titamin')]
#     ])
#
#
# cars = ["Cobalt", "Malibu", "Nexia"]
#
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/@titamin'))
#     return keyboard.adjust(2).as_markup()
