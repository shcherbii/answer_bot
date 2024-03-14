# from channels.generic.websocket import AsyncWebsocketConsumer
# import json
# from asgiref.sync import sync_to_async
# from django.contrib.auth.models import User
# from .models import ChatRoom, ChatMassages
# from .llm import get_vector, get_rag_promt, get_llm
# # from .views import model

# class ChatConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = f'chat{self.room_name}'

#         # model_llm = llm.crate_llm()

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
        
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.channel_layer,
#             self.room_group_name
#         )

#     async def receive(self,text_data):
        
#         data = json.loads(text_data)
        
#         message = data['message']
#         username = data['username']
#         room = data['room']

#         await self.channel_layer.group_send(
#             self.room_group_name,{
#                 'type':'chat_message',
#                 'message':message,
#                 'username':username,
#                 'room':room,
#             }
#         )
        

#         await self.save_massage(username, room, message)
        
#     async def chat_message(self, event):
#         message = event['message']
#         username = event['username']
#         room = event['room']

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message':message,
#             'username':username,
#             'room':room,
#         }))


#     @sync_to_async
#     def save_massage(self, username, room, message):
#         user = User.objects.get(username=username)
#         room = ChatRoom.objects.get(user=user)
#         ChatMassages.objects.create(user=user, room=room, massage_content = message)

