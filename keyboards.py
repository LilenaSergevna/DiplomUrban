from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выбрать питомца"),
            KeyboardButton(text="О нас"),
            KeyboardButton(text="Регистрация")
        ]
    ], resize_keyboard=True
)

catalog_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выбрать собаку", callback_data="all_dog")],
        [InlineKeyboardButton(text="Выбрать кошку", callback_data="all_cat")],
        [InlineKeyboardButton(text="Выбрать что то экзотическое", callback_data="all_other")]
    ]
)

dog_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Шпиц", callback_data="spitz")],
        [InlineKeyboardButton(text="Французкий бульдог", callback_data="bulldog")],
        [InlineKeyboardButton(text="Дворняга", callback_data="dvor")],
        [InlineKeyboardButton(text="Овчарка", callback_data="ovcharka")],
        [InlineKeyboardButton(text="Кане корсо", callback_data="cane_corso")]
    ]
)

cat_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Сиамская кошка", callback_data="siam")],
        [InlineKeyboardButton(text="Британская короткошёрстная кошка", callback_data="brit")],
        [InlineKeyboardButton(text="Мейн-кун", callback_data="mein")]
    ]
)

exotic_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Змеи", callback_data="snake")],
        [InlineKeyboardButton(text="Пауки", callback_data="spider")],
        [InlineKeyboardButton(text="Рыбки", callback_data="fish")],
        [InlineKeyboardButton(text="Попугайчики", callback_data="birt")],
        [InlineKeyboardButton(text="Слон", callback_data="slon")]
    ]
)



buy_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url = "https://ya.ru")],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]
    ]
)

buy_kb1=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url = "https://ya.ru")],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog1')]
    ]
)

admin_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи',callback_data='users')],
        [InlineKeyboardButton(text='Статистика',callback_data='stat')],
        [
            InlineKeyboardButton(text='Блокировака',callback_data='block'),
            InlineKeyboardButton(text='Разблокировка',callback_data='unblock')
        ]
    ]
)

