import base64

for i in range(-10, 10):
    data = {
        "email": "teach@gmail.com",
        "role": f'{i}',
        "username": "admin"
    }
    json_string = str(data)

    base64_encode = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')
#     print(json_string)
    print(base64_encode)
