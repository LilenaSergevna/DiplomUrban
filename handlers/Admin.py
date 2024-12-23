from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards import *
import texts
import db

class admins(StatesGroup):
    id = State()
    #ban = State()

class admins1(StatesGroup):
    id = State()
    #ban = State()

async def admin(message):
    await message.answer(texts.admin, parse_mode="HTML",reply_markup=admin_kb)


async def show_users(call):
    t = '''ID, UserName, age
➖➖➖➖➖➖➖➖➖'''
    num = 0
    for user in db.get_all_users():
        num+=1
        if user[4]==1:
            bl='блок'
        else:
            bl='норм'
        t += f'\n{num}. <code>{user[0]}</code> @{user[1]} <b>{user[2]}</b>      {bl}'
    await call.message.answer(t, parse_mode="HTML", reply_markup=admin_kb)
    await call.answer()

async def count_stat(call):
    await call.message.answer(f'Кол-во пользователей: {db.count_stat()}', reply_markup=admin_kb)
    await call.answer()



async def block_user(call):
    await call.message.answer(texts.ban_from_admin, reply_markup=types.ReplyKeyboardRemove())
    await call.answer()
    await admins.id.set()


async def ban1(message, state):
    await state.update_data(id=message.text)
    bl_user = await state.get_data()
    rez=db.add_to_block(bl_user['id'])
    await state.finish()
    if rez==True:
        await message.answer(f"Пользователь заблочен {message.text}", reply_markup=admin_kb)
    else:
        await message.answer(f"Несушествует пользователя {message.text}", reply_markup=admin_kb)

async def unblock_user(call):
    await call.message.answer(texts.unban_from_admin, reply_markup=types.ReplyKeyboardRemove())
    await call.answer()
    await admins1.id.set()


async def unban1(message, state):
    await state.update_data(id=message.text)
    unbl_user = await state.get_data()
    rez=db.remove_block(unbl_user['id'])
    await state.finish()
    if rez==True:
        await message.answer(f"Пользователь разблокирован {message.text}", reply_markup=admin_kb)
    else:
        await message.answer(f"Несушествует пользователя {message.text}", reply_markup=admin_kb)

