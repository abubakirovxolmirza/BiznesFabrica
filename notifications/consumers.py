# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# import logging

# logger = logging.getLogger(__name__)

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Join the notifications group
#         await self.channel_layer.group_add(
#             "notifications",
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave the notifications group
#         await self.channel_layer.group_discard(
#             "notifications",
#             self.channel_name
#         )

#     async def notify(self, event):
#         # Log the incoming event to debug
#         logger.debug(f"Received event: {event}")
        
#         # Ensure all keys in the event dictionary are strings
#         validated_event = {str(k): v for k, v in event.items()}

#         # Log the validated event to debug
#         logger.debug(f"Validated event: {validated_event}")

#         # Receive notification from group and send to WebSocket
#         message = validated_event['message']
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
