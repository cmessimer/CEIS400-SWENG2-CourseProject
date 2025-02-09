# Python UI Calls the C# API

import requests

BASE_URL = "http://localhost:5000/api/equipment"

def checkout_equipment(user_id, equipment_id):
    url = 'http://127.0.0.1:5000/checkout'
    payload = {
        'user_id': user_id,
        'equipment_id': equipment_id
    }
    response = requests.post(url, json=payload)
    return response.json().get('message')
