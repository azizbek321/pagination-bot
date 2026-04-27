from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import rasmlar

def PaginationButton(count):
    buttons = InlineKeyboardBuilder()
    if count > 0:
        buttons.add(InlineKeyboardButton(text="⬅️ ortga", callback_data=f'ortga_{count}'))
    buttons.add(InlineKeyboardButton(text="❌", callback_data=f"shu_{count}"))
    if count < len(rasmlar) - 1:
        buttons.add(InlineKeyboardButton(text="oldinga ➡️", callback_data=f"oldinga_{count}"))
    return buttons.as_markup() 