import requests
from config import API_URL


class APIClient:

    def predict(self, data: dict):
        try:
            response = requests.post(API_URL, json=data)
            response.raise_for_status()
            result = response.json()
            return result.get("prediction", "N/A")
        except Exception as e:
            print("Error:", e)
            return "ERROR"
