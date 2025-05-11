from django.conf import settings
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def trigger_aiogram_event(event_type: str, payload: dict):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "aiogram_events",
        {
            "type": "aiogram.events",
            "event_type": event_type,
            "payload": payload,
        }
    )