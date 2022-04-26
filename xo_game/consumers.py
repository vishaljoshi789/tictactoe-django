import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Game


class GameConsumers(WebsocketConsumer):
    def connect(self):
        self.game_group_name = self.scope['url_route']['kwargs']['gameid']
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name
        )
        self.game = Game.objects.get(gameid=self.game_group_name)
        self.accept()
        message = {
            'box1': self.game.box1,
            'box2': self.game.box2,
            'box3': self.game.box3,
            'box4': self.game.box4,
            'box5': self.game.box5,
            'box6': self.game.box6,
            'box7': self.game.box7,
            'box8': self.game.box8,
            'box9': self.game.box9
        }
        self.send(text_data=json.dumps({
            'type': 'Connection',
            'message': message
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message['type'] == "gamecells":
            async_to_sync(self.channel_layer.group_send)(
                self.game_group_name,
                {
                    'type': 'gameCells',
                    'message': message
                }
            )

        elif message['type'] == 'player_name':
            async_to_sync(self.channel_layer.group_send)(
                self.game_group_name,
                {
                    'type': 'playerName',
                    'message': message
                }
            )

    def gameCells(self, event):
        message = event['message']

        # message['turn'] =
        self.send(text_data=json.dumps({
            'type': 'cells',
            'message': message
        }))
        if message['cell'] == 'box1':
            self.game.box1 = message['symbol']
        elif message['cell'] == 'box2':
            self.game.box2 = message['symbol']
        elif message['cell'] == 'box3':
            self.game.box3 = message['symbol']
        elif message['cell'] == 'box4':
            self.game.box4 = message['symbol']
        elif message['cell'] == 'box5':
            self.game.box5 = message['symbol']
        elif message['cell'] == 'box6':
            self.game.box6 = message['symbol']
        elif message['cell'] == 'box7':
            self.game.box7 = message['symbol']
        elif message['cell'] == 'box8':
            self.game.box8 = message['symbol']
        elif message['cell'] == 'box9':
            self.game.box9 = message['symbol']
        self.game.save()

    def playerName(self, event):
        message = event['message']
        if self.game.player1 == '' or self.game.player1 == None:
            self.game.player1 = self.player_name
            self.game.player1_symbol = 'X'
            self.game.save()
        else:
            if self.game.player2 == '' or self.game.player2 == None:
                self.game.player2 = self.player_name
                self.game.player2_symbol = 'O'
                self.game.save()
        message['player1Name'] = [self.game.player1, self.game.player1_symbol]
        message['player2Name'] = [self.game.player2, self.game.player2_symbol]

        self.player_name = message['player']
        self.send(text_data=json.dumps({
            'type': 'playerName',
            'message': message
        }))

    def disconnect(self, code):
        # return super().disconnect(code)
        pass
