import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7427669932:AAHDDYBwKmW4o2RxVf6k9hGczYvYIzcG64w"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    await message.reply(f"salom {first_name} ")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

