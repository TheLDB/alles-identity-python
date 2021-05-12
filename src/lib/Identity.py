import requests
import json
import aiohttp


class Identity:
    def __init__(self, appID, token):
        global a
        global t
        a = appID
        t = token

    async def createFlow(self, callback, state):
        async with aiohttp.ClientSession() as session:
            async with session.post('https://identity.alles.cx/a/v1/flow', data={'callback': callback, 'state': state}, auth=aiohttp.BasicAuth(a, t)) as resp:
                res = await resp.json()
                token = res['token']
                redirectURl = f'https://identity.alles.cx/login?flow={token}'
                return redirectURl

    async def getProfile(self, code):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://identity.alles.cx/a/v1/profile?code=${code}', auth=aiohttp.BasicAuth(a, t)) as resp:
                return resp
