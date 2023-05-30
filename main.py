import logging
from testing import video_yuklab_ber
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6251993066:AAFG0CJmZsLUqOYDIvRsEK1Js7wrN-7Oucs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("you tubening oxirgi 11ta belgisini yozing")



@dp.message_handler()
async def echo(message: types.Message):
    mes_text = message.text
    video_link = video_yuklab_ber(mes_text)
    await message.answer_video(video_link)
 



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)