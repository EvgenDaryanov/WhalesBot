from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states.state_user import StorageUsers
from loader import bot
from data.db_api import sqlite
from keyboards.inline import inline_kb_main
from utils.utils_defs import createpayment
from filters.all_filters import isAdmin
from aiogram.types import FSInputFile
import random
import string
import imgbbpy


# DB INIT CLASSES
UserManager = sqlite.UserManager()


def generate_random_code(length):
    return ''.join(random.choice(string.hexdigits) for _ in range(length))

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
	await state.clear()

	user_meta = UserManager.get_userx(message.from_user.id)

	if user_meta == []:
		try:
			start_param = message.text.split(maxsplit=1)[1]
			referal_meta = UserManager.get_referalx(start_param)
		except:
			start_param = 'None'

		user_profile_photo: UserProfilePhotos = await bot.get_user_profile_photos(message.from_user.id)
		image_url = 'None'
		if user_profile_photo.total_count > 0:
			file = await bot.get_file(user_profile_photo.photos[0][0].file_id)
			await bot.download_file(file.file_path, f'img/{message.from_user.id}.png')
			client = imgbbpy.SyncClient('0e5610bd4c915d9b12d8e8bc76df3a1b')
			image = client.upload(file=f'img/{message.from_user.id}.png')
			image_url = image.url

		UserManager.add_userx(message.from_user.id, message.from_user.username, generate_random_code(16), start_param, image_url)

	if message.from_user.language_code == 'ru':

		video = FSInputFile("whale_promo_fixed.mp4")
		await message.answer_video(video=video, caption='''Привет!

Добро пожаловать в @whale, №1 Онлайн Казино!

🎰Более 300 популярных казино игр
💰Автоматизированные и мгновенные выводы
🏦 Поддержка TON и USDT!''', reply_markup=inline_kb_main.webappkb_inline(message.from_user.language_code))

	else:
		video = FSInputFile("whale_promo_fixed.mp4")
		await message.answer_video(video=video, caption='''Hi!

Welcome to @whale, the #1 Online Casino!

🎰 Over 300 popular casino games
💰Automated and instant withdrawals
🏦 Support TON and USDT!''', reply_markup=inline_kb_main.webappkb_inline(message.from_user.language_code))

@router.callback_query(F.data=='goto_start')
async def cmd_start(call: CallbackQuery, state: FSMContext):
	await state.clear()
	await call.message.delete()

	if call.from_user.language_code == 'ru':
		video = FSInputFile("whale_promo_fixed.mp4")
		await message.answer_video(video=video, caption='''Привет!

Добро пожаловать в @whale, №1 Онлайн Казино!

🎰Более 300 популярных казино игр
💰Автоматизированные и мгновенные выводы
🏦 Поддержка TON и USDT!''', reply_markup=inline_kb_main.webappkb_inline(call.from_user.language_code))

	else:
		video = FSInputFile("whale_promo_fixed.mp4")
		await message.answer_video(video=video, caption='''Hi!

Welcome to @whale, the #1 Online Casino!

🎰 Over 300 popular casino games
💰Automated and instant withdrawals
🏦 Support TON and USDT!''', reply_markup=inline_kb_main.webappkb_inline(call.from_user.language_code))

@router.callback_query(F.data=="whales_menu_earn")
async def call_whales_menu_earn(call: CallbackQuery, state: FSMContext):
	await state.clear()

	await call.message.delete()

	user_meta = UserManager.get_userx(call.from_user.id)
	get_kb = inline_kb_main.earnmoeny_kb_inline(user_meta[0][3], call.from_user.language_code)
	if call.from_user.language_code == 'ru':
		await call.message.answer('''Пригласи друга и заработай с @whale!

💰 Вы получаете 10% от краевой части с каждой прямой реферальной ссылки
💰 и 1% за каждую реферальную ссылку второго уровня!
💰 Заработанные средства выплачиваются ежемесячно''', reply_markup=get_kb)

	else:
		await call.message.answer('''Invite a friend and make money with @whale!

💰 You get 10% of the edge from each direct referral link
💰 and 1% for every second level referral link!
💰 Earnings are paid monthly''', reply_markup=get_kb)

@router.callback_query(F.data.startswith("whales_copy_referal"))
async def call_whales_copy_referal(call: CallbackQuery, state: FSMContext):
	await state.clear()

	referal_code = call.data.split(":")[1]

	await call.message.delete()

	await call.message.answer(f'<code>https://t.me/dispersedstudiotest_bot/?start={referal_code}</code>', reply_markup=inline_kb_main.backto_earnmoney_inline(call.from_user.language_code))


@router.callback_query(F.data.startswith("whales_menu_cash"))
async def call_whales_menu_cash(call: CallbackQuery, state: FSMContext):
	await state.clear()

	await call.message.delete()

	user_meta = UserManager.get_userx(call.from_user.id)

	if call.from_user.language_code == 'ru':
		await call.message.answer(f'''💵 Кошелёк

Баланс: {user_meta[0][5]} TON''', reply_markup=inline_kb_main.cashmenu_kb_inline(call.from_user.language_code))

	else:
		await call.message.answer(f'''💵 Wallet

Balance: {user_meta[0][5]} TON''', reply_markup=inline_kb_main.cashmenu_kb_inline(call.from_user.language_code))


@router.callback_query(F.data.startswith("cashout"))
async def call_whales_menu_cash(call: CallbackQuery, state: FSMContext):
	await state.clear()

	await call.message.delete()
	user_meta = UserManager.get_userx(call.from_user.id)

	if call.from_user.language_code == 'ru':
		await call.message.answer(f'''Ваш баланс {user_meta[0][5]} TON

Мы используем автоматические выводы! Если вы хотите сейчас вывести средства, пожалуйста, нажмите ниже

❗️Минимальная сумма вывода: 1.0 TON''', reply_markup=inline_kb_main.agree_withdraw(call.from_user.language_code))
	else:
		await call.message.answer(f'''Your balance {user_meta[0][5]} TON

We use automatic withdrawals! If you would like to withdraw now, please click below

❗️Minimum withdrawal amount: 1.0 TON''', reply_markup=inline_kb_main.agree_withdraw(call.from_user.language_code))

@router.callback_query(F.data.startswith("agreewithdraw"))
async def call_agreewithdraw(call: CallbackQuery, state: FSMContext):
	await state.clear()
	await call.answer(text='Processing.. ETA 1 minute')
	await call.message.delete()

	if call.from_user.language_code == 'ru':
		await call.message.answer('Ваш запрос на вывод был получен и скоро будет обработан!', reply_markup=inline_kb_main.goto_start(call.from_user.language_code))
	else:
		await call.message.answer('Your withdrawal request has been received and will be processed soon!', reply_markup=inline_kb_main.goto_start(call.from_user.language_code))



@router.callback_query(F.data=="cashin")
async def call_whales_menu_cash(call: CallbackQuery, state: FSMContext):
	await state.clear()

	await call.message.delete()

	if call.from_user.language_code == 'ru':
		await call.message.answer('''👉 Введите сумму для пополнения в TON

❗️Минимальный депозит: 1 TON''', reply_markup=inline_kb_main.goto_start(call.from_user.language_code))

	else:
		await call.message.answer('''👉 Enter the amount to deposit in TON

❗️Minimum deposit: 1 TON''', reply_markup=inline_kb_main.goto_start(call.from_user.language_code))


	await state.set_state(StorageUsers.get_amount)

@router.message(StorageUsers.get_amount, F.text)
async def state_get_amount(message: Message, state: FSMContext):
	amount = message.text
	try:
		number = int(amount)
	except:
		try:
			number = float(amount)
		except:

			number = False

	if number:
		if number >= 1:
			await state.clear()
			invoice_link = await createpayment(number, message.from_user.id)
			if message.from_user.language_code == 'ru':
				await message.answer(f'''💵 Депозит через @Cryptobot

	Сумма депозита: {number} TON''', reply_markup=inline_kb_main.pay_kb_inline(invoice_link, message.from_user.language_code))
			else:
				await message.answer(f'''💵 Deposit via @Cryptobot

	Deposit Amount: {number} TON''', reply_markup=inline_kb_main.pay_kb_inline(invoice_link, message.from_user.language_code))


@router.message(Command("admin"), isAdmin())
async def admin_panel(message: Message, state: FSMContext):
	await state.clear()

	await message.answer('Админ панель ебать', reply_markup=inline_kb_main.admin_panel_inline())

@router.callback_query(F.data=='admin_statistic', isAdmin())
async def admin_statistic(call: CallbackQuery, state: FSMContext):
	await state.clear()

	users = UserManager.get_usersx()

	await call.message.delete()

	user_strings = [f"💠 @{user[2]} | {user[1]}\n" for user in users]

	messages = []
	current_message = ""

	for user_string in user_strings:

		if len(current_message) + len(user_string) <= 4064:
			current_message += user_string
		else:
			messages.append(current_message)
			current_message = user_string

	if current_message:
	    messages.append(current_message)

	for i, msg in enumerate(messages):
		await call.message.answer(f'''<b>{i+1}. Список пользователей</b>
{msg}''')