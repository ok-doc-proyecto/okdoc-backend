import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

class WSconsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(3):
            self.send(json.dumps({'message':randint(1,100)}))
            sleep(1)
        self.disconnect(1234)
        pass