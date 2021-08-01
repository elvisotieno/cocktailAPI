from channels.generic.websocket import AsyncWebsocketConsumer


class CocktailConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('mygroup',self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('mygroup',self.channel_name)

    async def send_cocktails(self,event):
        cocktails_details = event['latest_cocktails']
        await self.send(cocktails_details)