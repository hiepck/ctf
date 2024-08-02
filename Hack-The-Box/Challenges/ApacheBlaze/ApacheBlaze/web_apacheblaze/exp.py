import requests

url = 'http://83.136.252.187:33474/'

header = {
    "X-Forwarded-Host": "dev.apacheblaze.local",
    "Referer": "http://83.136.252.187:33474/?game=click_topia"
}

res = requests.get(url, headers=header)

print(res.text)