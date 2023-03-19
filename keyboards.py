from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import *


def get_keyboard_start_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(START_BUT1)
    b2 = KeyboardButton(START_BUT2)
    b3 = KeyboardButton(START_BUT3)
    b4 = KeyboardButton(START_BUT4)
    b5 = KeyboardButton(START_BUT5)
    b6 = KeyboardButton(START_BUT6)
    b7 = KeyboardButton(START_BUT7)
    kb.add(b1, b2)
    kb.add(b3, b4)
    kb.add(b5, b6)
    kb.add(b7)
    return kb


def get_keyboard_back_to_start() -> ReplyKeyboardMarkup():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(BACK_TO_START_BUT)
    kb.add(b1)
    return kb


def get_keyboard_back_to_start_mind() -> ReplyKeyboardMarkup():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(BACK_TO_START_BUT_MIND)
    kb.add(b1)
    return kb


def get_keyboard_calculate() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(RUB_MONERO)
    b2 = KeyboardButton(MONERO_RUB)
    b3 = KeyboardButton(RUB_BITCOIN)
    b4 = KeyboardButton(BITCOIN_RUB)
    b5 = KeyboardButton(RUB_USDT)
    b6 = KeyboardButton(USDT_RUB)
    b7 = KeyboardButton(BACK_TO_START_BUT)
    kb.add(b1, b2)
    kb.add(b3, b4)
    kb.add(b5, b6)
    kb.add(b7)
    return kb

def get_keyboard_calculate_repeat_or_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(REPEAT_CALCULATE)
    b2 = KeyboardButton(BACK_TO_START_BUT)
    kb.add(b1)
    kb.add(b2)
    return kb


def get_keyboard_buy() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(MONERO)
    b2 = KeyboardButton(BTC)
    b3 = KeyboardButton(USDT)
    b4 = KeyboardButton(BACK_TO_START_BUT)
    kb.add(b1)
    kb.add(b2)
    kb.add(b3)
    kb.add(b4)
    return kb


def get_keyboard_buy_final() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(BUY_FINAL)
    b2 = KeyboardButton(BACK_TO_START_BUT_MIND)
    kb.add(b1)
    kb.add(b2)
    return kb


def get_keyboard_change_pay() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(CHANGE_PAY1)
    b2 = KeyboardButton(BACK_TO_START_BUT_MIND)
    kb.add(b1)
    kb.add(b2)
    return kb


def get_keyboard_channel_yes_no(label):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton('✅ Отработана', callback_data=f'order_check_{label}')
    ib2 = InlineKeyboardButton('❌ Отменить', callback_data=f'order_cancel_{label}')
    ikb.add(ib1, ib2)
    return ikb