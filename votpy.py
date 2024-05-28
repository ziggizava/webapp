import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
import logging
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6604816437:AAGo_8Sd2Sl6Sex6vWxFsC8WUrjFkrCRbhQ')
dp = Dispatcher()
router = Router()


@router.message(Command('start'))
async def start(message: Message):
    markup = (types.ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Открыть веб-страницу', web_app=WebAppInfo(url='https://harmonious-yeot-c7fa9f.netlify.app/'))], ],
        resize_keyboard=True,
        input_field_placeholder='Web-App'))
    await message.answer(f'Добро пожаловать в наш бот {message.from_user.first_name} {[message.from_user.username]} !',
                         reply_markup=markup)


async def main():  #
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  #
    try:
        asyncio.run(main())  #
    except KeyboardInterrupt:  #
        print('Exit')
