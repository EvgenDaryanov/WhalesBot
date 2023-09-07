import sqlite3
import time


path_to_db = '../data/db_api/base.sqlite'


class UserManager:

	def get_userx(self, user_id):
		with sqlite3.connect(path_to_db) as db:
			response = db.execute('''SELECT * FROM storage_users WHERE user_id = (?)''', [user_id]).fetchall()

		return response

	def add_userx(self, user_id, user_name, referal_code, referal, img):
		with sqlite3.connect(path_to_db) as db:
			db.execute('''INSERT INTO storage_users(user_id, username, referal_code, referal, image) VALUES (?,?,?,?,?)''', [user_id, user_name, referal_code, referal, img])

	def get_referalx(self, referal_code):
		with sqlite3.connect(path_to_db) as db:
			response = db.execute('''SELECT * FROM storage_users WHERE referal_code = (?)''', [referal_code]).fetchall()

		return response

	def get_usersx(self):
		with sqlite3.connect(path_to_db) as db:
			response = db.execute('''SELECT * FROM storage_users''').fetchall()

		return response

class InvoiceManager:

	def add_invoice(self, invoice_id, amount, user_id):
		with sqlite3.connect(path_to_db) as db:
			db.execute('''INSERT INTO storage_invoices(invoice_id, amount, status, user_id) VALUES(?,?,?,?)''', [invoice_id, amount, 'notpaid', user_id])

	def get_invoices(self):
		with sqlite3.connect(path_to_db) as db:
			response = db.execute('''SELECT * FROM storage_invoices WHERE status = (?)''', ['notpaid']).fetchall()

		return response

	def update_status(self, invoice_id, amount, user_id):
		with sqlite3.connect(path_to_db) as db:
			db.execute('''UPDATE storage_invoices SET status = (?) WHERE invoice_id = (?)''', ['paid', invoice_id])
			db.execute('''UPDATE storage_users SET balance = balance + (?) WHERE user_id = (?)''', [amount, user_id])

class AdminManager:

	def get_adminx(self, user_id):
		with sqlite3.connect(path_to_db) as db:
			response = db.execute('''SELECT * FROM storage_admins WHERE user_id = (?)''', [user_id]).fetchall()
		return response

	def get_adminsx(self):
		with sqlite3.connect(path_to_db) as db:
			response = db.execute('''SELECT * FROM storage_admins WHERE admin_level < 3''').fetchall()
		return response

	def add_adminx(self, user_id, user_name, joined_date, admin_level):
		with sqlite3.connect(path_to_db) as db:
			db.execute('''INSERT INTO storage_admins(user_id, user_name, joined_date, admin_level) VALUES(?,?,?,?)''', [user_id, user_name, joined_date, admin_level])

	def delete_adminx(self, user_id):
		with sqlite3.connect(path_to_db) as db:
			db.execute('''DELETE FROM storage_admins WHERE user_id = (?)''', [user_id])

	def change_admin_lvlx(self, user_id, admin_level):
		with sqlite3.connect(path_to_db) as db:
			db.execute('''UPDATE storage_admins SET admin_level = (?) WHERE user_id = (?)''', [admin_level, user_id])