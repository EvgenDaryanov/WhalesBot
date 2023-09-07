from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from data.db_api.sqlite import AdminManager

AdminManager = AdminManager()

class isAdmin(BaseFilter):
	async def __call__(self, message: Message) -> bool:
		admin = AdminManager.get_adminx(message.from_user.id)
		if admin != []:
			return True
		else:
			return False

