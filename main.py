from fastapi import FastAPI, Body
from data.db_api import sqlite
from fastapi.middleware.cors import CORSMiddleware
import utils_defs

# DB INIT
UserManager = sqlite.UserManager()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

@app.post("/items/")
async def create_item(item: dict = Body(...)):
    try:
        user_id = item["user_id"]
        user_id = int(user_id)

        user_data = UserManager.get_userx(user_id)

        if user_data == []:
            return {'error': 'User_id не найден'}
        else:
            return {'balance': user_data[0][5],
                    'image': user_data[0][6]}
    except:
        return {'error': 'User_id не найден'}

@app.post("/pay/")
async def pay_item(item: dict = Body(...)):
    try:
        user_id = item["user_id"]
        amount = item["amount"]
        amount = float(amount)
        user_id = int(user_id)

        user_data = UserManager.get_userx(user_id)

        url = await utils_defs.createpayment(amount, user_id)
        if user_data == []:
            return {'error': 'User_id не найден'}
        else:
            return {'url': url}
    except Exception as e:
        return {'error': f'Произошла ошибка: {e}'}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
