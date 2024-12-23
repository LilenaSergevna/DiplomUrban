import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyexpat.errors import messages

from config import *
from keyboards import *
import texts
import handlers.Start
import handlers.Admin
import db

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


dp.message_handler(lambda m: db.check_block(m.from_user.id))(handlers.Start.ban_message)
dp.callback_query_handler(lambda c: db.check_block(c.from_user.id))(handlers.Start.ban_callbackquery)

#message.answer_photo
#message.answer_video
#message.answer_file
dp.message_handler(commands=['start'])(handlers.Start.start)

dp.message_handler(text="О нас")(handlers.Start.about)

dp.message_handler(text="Выбрать питомца")(handlers.Start.price)

dp.callback_query_handler(text='all_dog')(handlers.Start.buy_dog)
dp.callback_query_handler(text='all_cat')(handlers.Start.buy_cat)
dp.callback_query_handler(text='all_other')(handlers.Start.buy_other)


dp.callback_query_handler(text='back_to_catalog')(handlers.Start.back_catalog)
dp.callback_query_handler(text='back_to_catalog1')(handlers.Start.buy_slon1)

#Регистрация
dp.message_handler(text='Регистрация')(handlers.Start.reg_user)

dp.message_handler(state=handlers.Start.RegistrationState.username)(handlers.Start.set_username)
dp.message_handler(state=handlers.Start.RegistrationState.age)(handlers.Start.set_age)



#Admin'ка
dp.message_handler(commands=['admin'])(handlers.Admin.admin)
dp.callback_query_handler(text=['users'])(handlers.Admin.show_users)
dp.callback_query_handler(text=['stat'])(handlers.Admin.count_stat)

dp.callback_query_handler(text=['block'])(handlers.Admin.block_user)
dp.message_handler(state=handlers.Admin.admins.id)(handlers.Admin.ban1)


dp.callback_query_handler(text=['unblock'])(handlers.Admin.unblock_user)
dp.message_handler(state=handlers.Admin.admins1.id)(handlers.Admin.unban1)


#Собаки
dp.callback_query_handler(text=['spitz'])(handlers.Start.buy_spitz)
dp.callback_query_handler(text=['bulldog'])(handlers.Start.buy_bulldog)
dp.callback_query_handler(text=['dvor'])(handlers.Start.buy_dvor)
dp.callback_query_handler(text=['ovcharka'])(handlers.Start.buy_ovcharka)
dp.callback_query_handler(text=['cane_corso'])(handlers.Start.buy_cane_corso)

#Кошки
dp.callback_query_handler(text=['siam'])(handlers.Start.buy_siam)
dp.callback_query_handler(text=['brit'])(handlers.Start.buy_brit)
dp.callback_query_handler(text=['mein'])(handlers.Start.buy_mein)

#Экзотика
dp.callback_query_handler(text=['snake'])(handlers.Start.buy_snake)
dp.callback_query_handler(text=['spider'])(handlers.Start.buy_spider)
dp.callback_query_handler(text=['fish'])(handlers.Start.buy_fish)
dp.callback_query_handler(text=['birt'])(handlers.Start.buy_birt)
dp.callback_query_handler(text=['slon'])(handlers.Start.buy_slon)


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)

