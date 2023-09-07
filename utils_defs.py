from aiocryptopay import AioCryptoPay, Networks
from data.db_api import sqlite
import asyncio

# DB INIT CLASSES
InvoiceManager = sqlite.InvoiceManager()

crypto = AioCryptoPay(token='117811:AAAOn2XnPtkbwLbZvKUq8Z6tBlP6P6RRsKl', network=Networks.MAIN_NET)

async def createpayment(amount, user_id):
    invoice = await crypto.create_invoice(asset='TON', amount=amount)
    InvoiceManager.add_invoice(invoice.invoice_id, amount, user_id)
    
    return invoice.pay_url
