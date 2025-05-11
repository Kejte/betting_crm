import redis
from backend.settings import REDIS_URL
import json

def send_fokrs_to_private_group():
    r = redis.Redis.from_url(REDIS_URL)
    
    event_data = {
        'type': 'send_fokrs_to_private_group',
        'payload': {}
    }

    r.publish('aiogram_events', json.dumps(event_data))
    