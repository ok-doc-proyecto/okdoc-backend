import json
from random import randint
from time import sleep
import asyncio

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class WSconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(9):
            await self.send(json.dumps({'message':i*10}))
#           await self.send(json.dumps({'message':randint(1,100)}))
#           await asyncio.sleep(randint(1,3))
        await self.disconnect(1234)
        pass