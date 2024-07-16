# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class TasksConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = 'tasks_group'
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type': 'task_message',
#                 'message': message
#             }
#         )

#     async def task_message(self, event):
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

# class BallsConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = 'balls_group'
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type': 'ball_message',
#                 'message': message
#             }
#         )

#     async def ball_message(self, event):
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

# class HistoryBallsConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = 'historyballs_group'
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type': 'historyball_message',
#                 'message': message
#             }
#         )

#     async def historyball_message(self, event):
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
