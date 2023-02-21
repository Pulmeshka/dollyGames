from main import dp
from aiogram import types


# elif message.text.lower() == '':
#         if not message.reply_to_message:
#             await message.reply('вы не ответили на сообщение пользователя🎃')
#         else:
#             name = message.from_user.first_name
#             reply_name = message.reply_to_message.from_user.first_name     
#             await message.answer(f'{name} <b></b> {reply_name}', parse_mode='HTML')

#--------------шаблон для новых команд---------------

@dp.message_handler()
async def rp_commands(message: types.Message):
    if message.text.lower() == 'обнять':
        if not message.reply_to_message:
            await message.reply('вы не ответили на сообщение пользователя🎃')
        else:
            name = message.from_user.first_name
            reply_name = message.reply_to_message.from_user.first_name     
            await message.answer(f'{name} <b>обнял</b> {reply_name}', parse_mode='HTML')

    elif message.text.lower() == 'ударить':
        if not message.reply_to_message:
            await message.reply('вы не ответили на сообщение пользователя🎃')
        else:
            name = message.from_user.first_name
            reply_name = message.reply_to_message.from_user.first_name     
            await message.answer(f'{name} <b>жёстко ударил</b> {reply_name}', parse_mode='HTML')

    elif message.text.lower() == 'кинуть':
        if not message.reply_to_message:
            await message.reply('вы не ответили на сообщение пользователя🎃')
        else:
            name = message.from_user.first_name
            reply_name = message.reply_to_message.from_user.first_name     
            await message.answer(f'{name} <b>оттолкнул от себя</b> {reply_name}', parse_mode='HTML')

    elif message.text.lower() == 'выкинуть':
        if not message.reply_to_message:
            await message.reply('вы не ответили на сообщение пользователя🎃')
        else:
            name = message.from_user.first_name
            reply_name = message.reply_to_message.from_user.first_name     
            await message.answer(f'{name} <b>выкинул</b> {reply_name} <b>как мусор</b>', parse_mode='HTML')
        
    elif message.text.lower() == 'оскорбить':
        if not message.reply_to_message:
            await message.reply('вы не ответили на сообщение пользователя🎃')
        else:
            name = message.from_user.first_name
            reply_name = message.reply_to_message.from_user.first_name     
            await message.answer(f'{name} <b>оскорбил матом</b> {reply_name}', parse_mode='HTML')

