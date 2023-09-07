import asyncio
import logging
from datetime import datetime
from colorama import Fore, Style, init
from handlers.users import user_router
from loader import bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from utils.utils_defs import check_invoice

init()

logging.basicConfig(level=logging.INFO)

#Запуск бота
async def main(bot):
	dp = Dispatcher(storage=MemoryStorage())
	dp.include_routers(user_router.router)
	asyncio.create_task(check_invoice())

	print(Fore.RED + f'Бот успешно запущен!\nТекущее время: {datetime.now()}\n\nБот: WhalesBot\n© EasyBots\n\n')

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)

	
if __name__ == "__main__":
	asyncio.run(main(bot))