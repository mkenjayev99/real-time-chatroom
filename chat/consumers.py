from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None

    async def connect(self):
        # Add the user to the chat group based on the room they want to join
        room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the chat group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # Handle received messages and broadcast them to the chat group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data,
            }
        )

    async def chat_message(self, event):
        # Send the received message to the WebSocket
        await self.send(text_data=event['message'])
