import requests
from wandb import env

from service import *

class Discord(Service):
    def __init__(self):
        self._discord_webhook_url = env.get("DISCORD_WEBHOOK")

    def send_notification(self,message):
        data = {
            "content": message,
            "username": "pysmle"
        }

        result = requests.post(self._discord_webhook_url, json=data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Error: {err}")