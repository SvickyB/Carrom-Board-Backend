# game/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .ai_logic import ai_choose_shot

class CarromGameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "game_channel"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data["player"] == "ai":
            ai_move = ai_choose_shot(data["board_state"])
            if ai_move:
                await self.send(json.dumps({"type": "ai_move", "move": ai_move}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    