from fastapi import FastAPI, Body
from data.db_api import sqlite

# DB INIT
UserManager = sqlite.UserManager()

app = FastAPI()

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
    else:
        return {'error': 'User_id не найден'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
