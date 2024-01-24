import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    #as soon as user req to connect this fn runs
    def connect(self):
        self.room_group_name="chat"
        user = self.scope['user']
        if user.is_anonymous: 
            return self.close(401)
        #user.is_online = True
        #user.save()
        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
        self.accept()


    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        #print('msg',message)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
        
    
    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        print('msg0',message)
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))

    #as soon as user disconnects this fn runs
    def disconnect(self, code):
        user = self.scope["user"]
        if user.is_anonymous:
            return ""
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,self.channel_name)
        #user.is_online = False
        #user.save()
        

