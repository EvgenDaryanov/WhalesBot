from loader import bot
from aiogram.types import Message, CallbackQuery
from aiocryptopay import AioCryptoPay, Networks
from keyboards.inline import inline_kb_main
from data.db_api import sqlite
import asyncio

# DB INIT CLASSES
InvoiceManager = sqlite.InvoiceManager()

crypto = AioCryptoPay(token='117811:AAAOn2XnPtkbwLbZvKUq8Z6tBlP6P6RRsKl', network=Networks.MAIN_NET)

async def example_utils():
    pass

async def createpayment(amount, user_id):
    invoice = await crypto.create_invoice(asset='TON', amount=amount)
    InvoiceManager.add_invoice(invoice.invoice_id, amount, user_id)
    
    return invoice.pay_url

async def check_invoice():
    while True:

        invoices = InvoiceManager.get_invoices()

        for i in invoices:
            invoice = await crypto.get_invoices(invoice_ids=i[1])
            if invoice[0].status == 'paid':
                InvoiceManager.update_status(i[1], i[2], i[4])
                await bot.send_message(i[4], '✅ Deposit succeful')

        await asyncio.sleep(300)
