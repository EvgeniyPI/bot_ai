# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, executor, types
from usl_razchet import is_digit,rachet_vod
logging.basicConfig(level=logging.INFO)
bot = Bot(token="984505094:AAEOzAjSltD8mnYLrK6kKseFbNy9iCpdBRs")
dp = Dispatcher(bot)
@dp.message_handler(content_types=['text'])
async def main(message : types.Message):
    string = message.text
    #print(is_digit(string))
    if is_digit(string) == True:
        b = rachet_vod(string)
        await bot.send_message(message.from_user.id,b )
    else:
        await bot.send_message(message.from_user.id, 'Не число (число должно быть с точкой и без пробелов')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)