# Python UI Calls the C# API

import requests

BASE_URL = "http://localhost:5000/api/equipment"

def checkout_equipment(user_id, equipment_id):
    payload = {"UserID": user_id, "EquipmentID": equipment_id}
    response = requests.post(f"{BASE_URL}/checkout", json=payload)
    return response.json()
