import logging

from aiogram import Bot, Dispatcher, executor, types
from tester import video_yuklash
API_TOKEN = '6251993066:AAFG0CJmZsLUqOYDIvRsEK1Js7wrN-7Oucs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Bu tiktok bot")



@dp.message_handler()
async def echo(message: types.Message):
    mes_text = message.text
    video_link = video_yuklash(mes_text)
    await message.answer_video(video_link, "Zo'r video")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




