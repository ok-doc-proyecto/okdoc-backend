import json
from random import randint
from time import sleep
import asyncio

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class WSconsumer_test(AsyncWebsocketConsumer):
    counter = 0

    async def connect(self):
        await self.accept()
        w_aux = self.channel_layer
        await self.send(json.dumps({'message': 1}))
        await self.send(json.dumps({'message': 7}))
#       for i in range(9):
#           await self.send(json.dumps({'message':i*10}))
#           await self.send(json.dumps({'message':randint(1,100)}))
#           await asyncio.sleep(randint(1,3))
#        await asyncio.sleep(30)
#        await self.disconnect(1234)
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        nro = text_data_json['numero']
        message = text_data_json['message']
        username = text_data_json['username']
        self.counter += 1
        if self.counter < 15:
            await self.send(json.dumps({'message': (1000)}))
            await self.send(json.dumps({'message': (nro + 1)}))
        else:
            await self.disconnect(1234)
        pass


class WSconsumer(AsyncWebsocketConsumer):
    counter = 0

    async def connect(self):
        await self.accept()
        w_aux = self.channel_layer
        await self.send(json.dumps({'message': 1}))
        await self.send(json.dumps({'message': 7}))
#       for i in range(9):
#           await self.send(json.dumps({'message':i*10}))
#           await self.send(json.dumps({'message':randint(1,100)}))
#           await asyncio.sleep(randint(1,3))
#        await asyncio.sleep(30)
#        await self.disconnect(1234)
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        nro = text_data_json['numero']
        message = text_data_json['message']
        username = text_data_json['username']
        self.counter += 1
        if self.counter < 15:
            await asyncio.sleep(1)
            await self.send(json.dumps({'message': (1000)}))
            await self.send(json.dumps({'message': (nro + 1)}))
        else:
            await self.disconnect(1234)
        pass
