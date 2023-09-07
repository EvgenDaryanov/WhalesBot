from aiogram import Bot
from data import config
import asyncio

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
