from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import *
import texts
import db


class RegistrationState(StatesGroup):
    username=State()
    age=State()


async def start(message):
    await message.answer(f'Добро пожаловать <b> @{message.from_user.first_name} </b>' + texts.start, parse_mode="HTML",reply_markup=start_kb)

#message.answer_photo
#message.answer_video
#message.answer_file


async def about(message):
    with open('file_img/about.png', "rb") as img:
        await message.answer_photo(img, texts.about, reply_markup=start_kb)


async def price(message):
    await message.answer("Что вас интересует?", reply_markup=catalog_kb)

async def buy_dog(call):
    with open('file_img/all_dog.png', "rb") as img:
        await call.message.answer_photo(img, texts.about_dog, reply_markup=dog_kb)
        await call.answer()

async def buy_cat(call):
    with open('file_img/all_cat.png', "rb") as img:
        await call.message.answer_photo(img, texts.about_cat, reply_markup=cat_kb)
        await call.answer()

async def buy_other(call):
    if db.get_user(call.from_user.id):
        with open('file_img/other.png', "rb") as img:
            await call.message.answer_photo(img, texts.other, reply_markup=exotic_kb)
            await call.answer()
    else:
        await call.message.answer(texts.other_no_reg, reply_markup=catalog_kb)
        await call.answer()


async def back_catalog(call):
    await call.message.answer("Что вас интересует?", reply_markup=catalog_kb)
    await call.answer()

async def back_catalog(call):
    await call.message.answer("Что вас интересует?", reply_markup=catalog_kb)
    await call.answer()

"""Тут ведем регистрацию"""
async def reg_user(message):
    #проверка на регситрацию этого ID
    if db.get_user(message.from_user.id) ==True:
        await message.answer(f'Так мы с вами уже знакомы {message.from_user.first_name}. Может уже переудем уже к подбору питомца?')
        await message.answer("Что вас интересует?", reply_markup=catalog_kb)
    else:
        await message.answer(f'Введите имя пользователя:')
        await RegistrationState.username.set()

async def set_username(message, state):
    await state.update_data(username=message.text)
    await message.answer(f'Введите возраст')
    await RegistrationState.age.set()

async def set_age(message, state):
    await state.update_data(age=message.text)
    new_user = await state.get_data()
    db.add_user(message.from_user.id,new_user['username'], new_user['age'])
    await message.answer(f'Пользователь удачно зарегистрирован!')
    await state.finish()
    await message.answer("Что вас интересует?", reply_markup=catalog_kb)

"""Сообщение о блокировке"""
async def ban_message(update):
    await update.answer(texts.ban)


async def ban_callbackquery(update):
    await update.message.answer(texts.ban)
    await update.answer()



"""Собаки"""
async def buy_spitz(call):
    with open('file_img/spitz.png', "rb") as img:
        await call.message.answer_photo(img, texts.spitz, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_bulldog(call):
    with open('file_img/bulldog.png', "rb") as img:
        await call.message.answer_photo(img, texts.bulldog, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_dvor(call):
    with open('file_img/dvor.png', "rb") as img:
        await call.message.answer_photo(img, texts.dvor, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_ovcharka(call):
    with open('file_img/ovcharka.png', "rb") as img:
        await call.message.answer_photo(img, texts.ovcharka, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_cane_corso(call):
    with open('file_img/cane_corso.png', "rb") as img:
        await call.message.answer_photo(img, texts.cane_corso, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()


"""Кошки"""
async def buy_siam(call):
    with open('file_img/siam.png', "rb") as img:
        await call.message.answer_photo(img, texts.siam, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_brit(call):
    with open('file_img/brit.png', "rb") as img:
        await call.message.answer_photo(img, texts.brit, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_mein(call):
    with open('file_img/mein.png', "rb") as img:
        await call.message.answer_photo(img, texts.mein, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

"""Экзотика"""""
async def buy_snake(call):
    with open('file_img/snake.png', "rb") as img:
        await call.message.answer_photo(img, texts.snake, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_spider(call):
    with open('file_img/spider.png', "rb") as img:
        await call.message.answer_photo(img, texts.spider, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_fish(call):
    with open('file_img/fish.png', "rb") as img:
        await call.message.answer_photo(img, texts.fish, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_birt(call):
    with open('file_img/birt.png', "rb") as img:
        await call.message.answer_photo(img, texts.birt, parse_mode="HTML", reply_markup=buy_kb)
        await call.answer()

async def buy_slon(call):
    with open('file_img/slon.png', "rb") as img:
        await call.message.answer_photo(img, texts.slon, parse_mode="HTML", reply_markup=buy_kb1)
        await call.answer()

async def buy_slon1(call):
    with open('file_img/slon.png', "rb") as img:
        await call.message.answer_photo(img, texts.slon1, parse_mode="HTML", reply_markup=buy_kb1)
        await call.answer()