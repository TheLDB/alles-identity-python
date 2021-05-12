import os
from Identity import Identity
from dotenv import load_dotenv

import asyncio

load_dotenv('.env')

APP_ID = os.environ.get('APP_ID')
TOKEN = os.environ.get('SECRET')
process = Identity(APP_ID, TOKEN)


async def createFlow():
    res = await process.createFlow('http://localhost:8080/callback', 'state')
    print(res)


async def getUser():
    res = await process.getProfile('')
    print(res)


asyncio.run(createFlow())
