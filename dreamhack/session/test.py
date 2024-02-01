for i in range(256):
    byte_value = i.to_bytes(1, byteorder='big')
    hex_value = byte_value.hex()
    print(f"{hex_value}")