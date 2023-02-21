from aiogram import types, Bot, Dispatcher, executor

bot = Bot(token='6149540213:AAHIIBpCO5imP3d8uU50kbRKn1ft2uF2p6M')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp
    print('started')
    executor.start_polling(dp)