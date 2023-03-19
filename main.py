from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified
from dotenv import load

import os

from keyboards import *
from utils import *


load()

storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)


NAME_BOT = 'DemonstrationWorkBot'


class StateUsersData(StatesGroup):
    Calculate_RUB_BTC = State()
    RewievState = State()
    BuyMONERO = State()

class BuyMonero(StatesGroup):
    inputMonero = State()
    inputChangePay = State()
    inputMoneroWallet = State()
    finalMonero = State()


# MONERO
# BITCOIN
# USDT


# async def edit_text_message(message: types.Message, text: str, keyboard: types.ReplyKeyboardMarkup):
#     with suppress(MessageNotModified):
#         await message.edit_text(text, reply_markup=keyboard())


@dp.message_handler(commands=['start'])
async def command_start_process(message: types.Message):
    if message.text[7:]:
        # куда то записываем парнерские данные
        pass
    text = START_TEXT
    await message.answer(text, reply_markup=get_keyboard_start_menu())


@dp.message_handler(Text(equals=[BACK_TO_START_BUT, BACK_TO_START_BUT_MIND]), state='*')
async def command_back_to_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    text = START_TEXT
    await message.answer(text, reply_markup=get_keyboard_start_menu())


@dp.message_handler(Text(equals=START_BUT7))
async def command_referal_process(message: types.Message):
    # запрос к базе данных о рефералах
    # добавить user_id 
    text = f"Вы пригласили <b>0</b> человек\nВаша ссылка реферальная ссылка\n\n<b>Нажмите на нее, чтобы скопировать</b>\n\n<code>https://t.me/{NAME_BOT}?start=11111111</code>"
    await message.answer(text, reply_markup=get_keyboard_back_to_start())


@dp.message_handler(Text(equals=START_BUT6))
async def command_faq_process(message: types.Message):
    text = f"Информация как пользоваться сервисом"
    await message.answer(text, reply_markup=get_keyboard_back_to_start())


@dp.message_handler(Text(equals=START_BUT3))
async def command_about_process(message: types.Message):
    text = f"Информация о сервисе\nКакие то ссылки и тд."
    await message.answer(text, reply_markup=get_keyboard_back_to_start())


# РАЗДЕЛ С ОТЗЫВАМИ

@dp.message_handler(Text(equals=START_BUT5))
async def command_rewiev_process(message: types.Message, state: FSMContext):
    text = "Напишите Ваш отзыв"
    await message.answer(text, reply_markup=get_keyboard_back_to_start())
    await state.set_state(StateUsersData.RewievState.state)


@dp.message_handler(state=StateUsersData.RewievState)
async def ckeck_rewiev(message: types.Message, state: FSMContext):
    rewiev = message.text
    print(rewiev)
    # записываем или пересылаем отзыв куда то
    text = "Спасибо, Ваш отзыв отправлен на модерацию"
    await message.answer(text, reply_markup=get_keyboard_back_to_start())
    await state.finish()

# КОНЕЦ РАЗДЕЛА С ОТЗЫВАМИ

# РАЗДЕЛ С КАЛЬКУЛЯТОРОМ ВАЛЮТ

@dp.message_handler(Text(equals=START_BUT4))
async def command_calculate_process(message: types.Message):
    text = f"Выберете направление"
    await message.answer(text, reply_markup=get_keyboard_calculate())


@dp.message_handler(Text(equals=RUB_MONERO))
async def command_calculate_rub_monero_process(message: types.Message, state: FSMContext):
    text = f"Введите сумму в рублях"
    await state.set_state(StateUsersData.Calculate_RUB_BTC.state)
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=StateUsersData.Calculate_RUB_BTC)
async def check_rub_monero(message: types.Message, state: FSMContext):
    rub: str = message.text
    if rub.isdigit():
        btc = "0.0123"
        # функция перевода рублей в биткоины
        text = f"{rub} рублей это {btc} BTC"
        await message.answer(text, reply_markup=get_keyboard_calculate_repeat_or_start())
        await state.finish()
    else:
        text = f"Вы ввели не корректную сумму\nПопробуйте еще раз\n\n<i>Пример:</i> 20000"
        await message.answer(text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=REPEAT_CALCULATE))
async def command_repeat_calculate(message: types.Message, state: FSMContext):
    await message.delete()
    text = f"Выберете направление"
    await message.answer(text, reply_markup=get_keyboard_calculate())


# КОНЕЦ РАЗДЕЛА КАЛЬКУЛЯТОРА ВАЛЮТ

# РАЗДЕЛ С ПОКУПКОЙ ВАЛЮТЫ

@dp.message_handler(Text(equals=START_BUT1))
async def command_buy_process(message: types.Message):
    text = "Выберете, что хотите купить"
    await message.answer(text, reply_markup=get_keyboard_buy())


@dp.message_handler(Text(equals=MONERO))
async def command_buy_monero_process(message: types.Message, state: FSMContext):
    # делаем запрос к API узнаем текущий курс биткоина

    text = f"""📈 Текущий курс 
1 MONERO = 2304720 руб + 50 руб

Сколько вы хотите купить MONERO? 
Введите количество монет
в формате X.ХХХХ
 
 <i>Пример:</i>  0.055"""

    await message.answer(text, reply_markup=get_keyboard_back_to_start())
    await state.set_state(BuyMonero.inputMonero.state)


@dp.message_handler(state=BuyMonero.inputMonero)
async def check_rub_monero(message: types.Message, state: FSMContext):
    rub: float = message.text
    # проверка на формат Х.ХХХХ
    # првоерка что в банке есть столько денег
    print(rub)
    text = "Выберете способ оплаты"
    await message.answer(text, reply_markup=get_keyboard_change_pay())
    await BuyMonero.next()


@dp.message_handler(state=BuyMonero.inputChangePay)
async def check_rub_monero_change_pay(message: types.Message, state: FSMContext):
    change_pay = message.text
    # записали в дату
    text = "Введите адрес своего кошелька для получения"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await BuyMonero.next()


@dp.message_handler(state=BuyMonero.inputMoneroWallet)
async def check_rub_monero_wallet(message: types.Message, state: FSMContext):
    wallet: str = message.text
    # проверка на формат кошелька
    print(wallet)
    count_rub = 1234 # считывает из даты
    count_monero = 12
    text = f"""<b>Ваша заявка действует 20 минут</b>

Вам необходимо сделать преевод
на карту: <code>2202206191497150</code>

<i>Нажмите на номер карты, чтобы скопировать</i>

На сумму: <code>{count_rub}</code>
Вам зачислиться: {count_monero} MONERO

Текст.
    """
    await message.answer(text, reply_markup=get_keyboard_buy_final())
    await BuyMonero.next()



@dp.message_handler(Text(equals=BUY_FINAL), state=BuyMonero.finalMonero)
async def check_rub_monero_wallet_final(message: types.Message, state: FSMContext):
    # отправляем в канал анкету для подтверждения
    print('Отправил анкету на расмотрение')
    text = "Ваша заявка на обмен принята\nОжидайте в течении 20 минут средства на вашем кошельке"
    await message.answer(text, reply_markup=get_keyboard_back_to_start_mind())


# КОНЕЦ РАЗДЕЛА

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)