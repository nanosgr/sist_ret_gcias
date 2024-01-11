from fastapi import FastAPI

from app.users.users import router_users
from app.aeronaves.aeronaves import router_aeronaves
from app.auth.auth import router_auth

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_aeronaves)

@app.get('/')
async def root():
    return 'Anda OK!'