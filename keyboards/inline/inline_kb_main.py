from aiogram.types import InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.db_api.sqlite import *
import json

adjustval = 2
count_list_page = 10 * adjustval

def example_inline_kb():
	keyboard = InlineKeyboardBuilder()

	keyboard.row(InlineKeyboardButton(text='Пример', callback_data=f'example'))

	return keyboard.as_markup()

def webappkb_inline(lang):
	keyboard = InlineKeyboardBuilder()

	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='🔥 Играть Сейчас 🔥', web_app=WebAppInfo(url='https://96be-109-89-208-58.ngrok-free.app')))
		keyboard.row(InlineKeyboardButton(text='💰 Заработать 💰', callback_data='whales_menu_earn'), InlineKeyboardButton(text='👛 Кошелек 👛', callback_data='whales_menu_cash'))
		keyboard.row(InlineKeyboardButton(text='💭 Присоединяйтесь к сообществу 💭', url='https://t.me/whalesocials'))
	else:
		keyboard.row(InlineKeyboardButton(text='🔥 Play Now 🔥', web_app=WebAppInfo(url='https://96be-109-89-208-58.ngrok-free.app')))
		keyboard.row(InlineKeyboardButton(text='💰 Earn 💰', callback_data='whales_menu_earn'), InlineKeyboardButton(text='👛 Wallet 👛', callback_data='whales_menu_cash'))
		keyboard.row(InlineKeyboardButton(text='💭 Join the community 💭', url='https://t.me/whalesocials'))

	return keyboard.as_markup()

def earnmoeny_kb_inline(referal_code, lang):
	keyboard = InlineKeyboardBuilder()

	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='Поделиться', switch_inline_query=f"Hi! You've been invited to @Whale , #1 Online casino in telegram! Join today !\n\n✅ https://t.me/dispersedstudiotest_bot/?start={referal_code}"), InlineKeyboardButton(text='Копировать', callback_data=f'whales_copy_referal:{referal_code}'))
		keyboard.row(InlineKeyboardButton(text='Статистика', web_app=WebAppInfo(url='https://96be-109-89-208-58.ngrok-free.app/profile/refferal-system')))
		keyboard.row(InlineKeyboardButton(text='« Назад', callback_data='goto_start'))
	else:
		keyboard.row(InlineKeyboardButton(text='Share', switch_inline_query=f"Hi! You've been invited to @Whale , #1 Online casino in telegram! Join today !\n\n✅ https://t.me/dispersedstudiotest_bot/?start={referal_code}"), InlineKeyboardButton(text='Copy', callback_data=f'whales_copy_referal:{referal_code}'))
		keyboard.row(InlineKeyboardButton(text='Statistics', web_app=WebAppInfo(url='https://96be-109-89-208-58.ngrok-free.app/profile/refferal-system')))
		keyboard.row(InlineKeyboardButton(text='« Back', callback_data='goto_start'))

	return keyboard.as_markup()

def backto_earnmoney_inline(lang):
	keyboard = InlineKeyboardBuilder()

	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='« Назад', callback_data='whales_menu_earn'))
	else:
		keyboard.row(InlineKeyboardButton(text='« Back', callback_data='whales_menu_earn'))

	return keyboard.as_markup()


def cashmenu_kb_inline(lang):
	keyboard = InlineKeyboardBuilder()
	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='📥 Депозит', callback_data='cashin'), InlineKeyboardButton(text='📤 Вывод', callback_data='cashout'))
		keyboard.row(InlineKeyboardButton(text='📖 Руководство', url='https://96be-109-89-208-58.ngrok-free.app'))
		keyboard.row(InlineKeyboardButton(text='« Назад', callback_data='goto_start'))
	else:
		keyboard.row(InlineKeyboardButton(text='📥 Deposit', callback_data='cashin'), InlineKeyboardButton(text='📤 Withdraw', callback_data='cashout'))
		keyboard.row(InlineKeyboardButton(text='📖 Manual', url='https://96be-109-89-208-58.ngrok-free.app'))
		keyboard.row(InlineKeyboardButton(text='« Back', callback_data='goto_start'))

	return keyboard.as_markup()

def agree_withdraw(lang):
	keyboard = InlineKeyboardBuilder()
	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='Подтвердите вывод', callback_data='agreewithdraw'))
		keyboard.row(InlineKeyboardButton(text='« Назад', callback_data='whales_menu_cash'))
	else:
		keyboard.row(InlineKeyboardButton(text='Confirm withdraw', callback_data='agreewithdraw'))
		keyboard.row(InlineKeyboardButton(text='« Back', callback_data='whales_menu_cash'))

	return keyboard.as_markup()

def goto_start(lang):
	keyboard = InlineKeyboardBuilder()

	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='« Назад', callback_data='goto_start'))
	else:
		keyboard.row(InlineKeyboardButton(text='« Back', callback_data='goto_start'))

	return keyboard.as_markup()

def pay_kb_inline(invoice_link, lang):
	keyboard = InlineKeyboardBuilder()

	if lang == 'ru':
		keyboard.row(InlineKeyboardButton(text='Оплатить через @Cryptobot', url=invoice_link))
		keyboard.row(InlineKeyboardButton(text='👾 Главное меню', callback_data='goto_start'), InlineKeyboardButton(text='« Назад', callback_data='whales_menu_cash'))
	else:
		keyboard.row(InlineKeyboardButton(text='Pay via @Cryptobot', url=invoice_link))
		keyboard.row(InlineKeyboardButton(text='👾 Main menu', callback_data='goto_start'), InlineKeyboardButton(text='« Back', callback_data='whales_menu_cash'))

	return keyboard.as_markup()

def admin_panel_inline():
	keyboard = InlineKeyboardBuilder()

	keyboard.row(InlineKeyboardButton(text='Статистика📊', callback_data='admin_statistic'))
	#keyboard.row(InlineKeyboardButton(text='Рассылка💬', callback_data='admin_rassilka'))

	return keyboard.as_markup()