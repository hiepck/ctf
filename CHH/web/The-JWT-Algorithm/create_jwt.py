import jwt

# Payload của JWT
payload = {
    "username": "admin",
}

# Tạo JWT với thuật toán 'none'
token = jwt.encode(payload, key=None, algorithm='none')

print("JWT token:", token)

# Giải mã JWT với thuật toán 'none'
decoded_payload = jwt.decode(token, key=None, algorithms=['none'])

print("Decoded payload:", decoded_payload)