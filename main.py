import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from config import bot_token
from buttons import PaginationButton
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from database import rasmlar


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command('start', prefix="/"))
async def cmd_start(message: types.Message):
    await message.answer_photo(photo=rasmlar[0], caption="Bu ajoyib rasmlar", reply_markup=PaginationButton(count=0))

@dp.callback_query(F.data)
async def PaginationButtonsBot(call: types.CallbackQuery):
    xabar = call.data.split("_")
    count = int(xabar[-1])
    if xabar[0] == "oldinga":
        count += 1
        await call.message.edit_media(
            InputMediaPhoto(media=rasmlar[count],
            caption=f"bu rasmlardagi {count + 1}"
                            ),
            reply_markup=PaginationButton(count=count)
        )
    elif xabar[0] == "ortga":
        count -= 1
        await call.message.edit_media(
            InputMediaPhoto(media=rasmlar[count],
            caption=f"bu rasmlardagi {count}"
                            ),
            reply_markup=PaginationButton(count=count)
        )
    else:
        await call.answer(f"sizning buyurtma {count}")
        await call.message.delete()


async def main():
    await bot.send_message(chat_id=7072212883, text="bot ishladi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")