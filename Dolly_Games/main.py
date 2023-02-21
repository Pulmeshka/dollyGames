from aiogram import types, Bot, Dispatcher, executor

bot = Bot(token='6149540213:AAHIIBpCO6M')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp
    print('started')
    executor.start_polling(dp)
