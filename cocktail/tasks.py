import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


# This function makes a request to an api responsible for obtaining 10 latest cocktails
@shared_task
def get_10lastest_cocktails():
    url = 'http://127.0.0.1:8000/cocktail/endpoint-cocktails'
    response = requests.get(url).json()
    cocktails =response
    async_to_sync(channel_layer.group_send)('mygroup',{'type':'send_cocktails', 'latest_cocktails':cocktails})