import os

# Tạo một byte ngẫu nhiên
random_byte = os.urandom(1)

# Chuyển đổi byte thành chuỗi hex
hex_string = random_byte.hex()

# In ra mã hex
print(hex_string)
