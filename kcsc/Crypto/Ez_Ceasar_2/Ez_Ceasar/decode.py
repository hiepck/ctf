import string
import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!{_}?"
ct = "ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O"

def decrypt(ct, key):
    pt = ""
    for i in ct:
        pt += (alphabet[(alphabet.index(i) - key) % len(alphabet)])
    return pt

# Thử tất cả các giá trị khóa từ 1 đến 25
for possible_key in range(1, 2**256):
    decrypted_message = decrypt(ct, possible_key)
    if decrypted_message.startswith('KCSC'):
        print(f"Key {possible_key}: {decrypted_message}")
