import requests


class N8NClient:

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_text(self, text):

        response = requests.post(
            self.webhook_url,
            json={
                "text": text
            },
            timeout=120,
        )

        print(f"📡 n8n status: {response.status_code}")
        print(f"📦 n8n raw response: {response.text!r}")

        response.raise_for_status()

        data = response.json()

        # n8n AI Agent returns a list
        if isinstance(data, list):
            return data[0]["output"]

        return data.get("output") or data.get("message")