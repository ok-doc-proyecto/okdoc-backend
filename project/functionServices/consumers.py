import json
import copy
from random import randint
from time import sleep
import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer


jsonSample = {
    "origin": {"socket": ""},
    "function": {"name": ""},
    "request": {"control": {}, "body": {}},
    "response": {"control": {}, "body": {}}
}


def jsonFunc(func):
    def inner(x_self, text_data=None, bytes_data=None):
        return func(x_self, text_data=None, bytes_data=None)
    return inner


async def asyncNoop(): pass


async def firstTest(pParam):
    wReturn = {}
    wReturn["control"] = pParam["control"]
    wReturn["body"] = copy.deepcopy(pParam["body"])
    return wReturn

funcMaps = {
    "noop": {"func": asyncNoop, "Atrbs": ["AlmostNoop", "jsonInOut"], },
    "firstTest": {"func": firstTest, "Atrbs": ["HighProcess", "jsonInOut"], },
}


async def processRequestAsync(pRequest):
    wNomFunc = pRequest["function"]["name"]
    wFuncion = funcMaps["wNomFunc"]["func"]
    wFuncRequest = pRequest["request"]
    wFuncRequest["control"]["origin"] = pRequest["origin"]
    wFuncRequest["control"]["messId"] = pRequest["control"]["messId"]
    wResponse = await wFuncion(wFuncRequest)
    wResponse["control"]["messIdGenerator"] = wFuncRequest["control"]["messId"]
    wSocket = pRequest["origin"]["socket"]
    await wSocket.controledSendJson(wResponse)
    return


class MyConsumer(AsyncWebsocketConsumer):
    groups = ["broadcast"]

    async def controledSendJson(self, pMessage):
        # agregar aca la logica de reintentos
        await self.send(json.dumps(pMessage))
        return

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()
#       await self.accept("subprotocol")
#       await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        wRequest = json.loads(text_data)
        # las funciones reciben el socket que las llamo
        wRequest["origin"]["socket"] = self
        processRequestAsync(wRequest)
        return
        # Called with either text_data or bytes_data for each frame
        # You can call:
#       await self.send(text_data="Hello world!")
#       await self.send(bytes_data="Hello world!")
#       await self.close()
#       await self.close(code=4123)

    async def disconnect(self, close_code):
        # Called when the socket closes
        await self.close(code=4123)
