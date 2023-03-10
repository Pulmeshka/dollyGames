from main import dp
from aiogram import types
from .data import Database

db = Database()
@dp.message_handler()
async def profile(message: types.Message):
    id = message.from_user.id
    dolly = db.get_balance(id)
    minti = db.get_minti(id)
    if message.text.lower() == 'ми':
        if db.get_balance(message.from_user.id) is None:
            db.insert_user(message.from_user.id)
        else:
            await message.answer(f'профиль {message.from_user.first_name}\nдолли🧿 - {dolly}\nминтиⓂ - {minti}\nбрак💞 - скоро...')
