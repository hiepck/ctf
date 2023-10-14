def decimal_to_binary(decimal):
    if decimal == 0:
        return '0b0'  # Trường hợp đặc biệt khi số thập phân là 0

    binary = ''
    sign = '-' if decimal < 0 else ''  # Xác định dấu cho số âm
    decimal = abs(decimal)  # Chuyển số âm thành số dương để chuyển đổi

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return f'0b{sign}{binary}'

# Ví dụ sử dụng
decimal_number = 293954012
binary_representation = decimal_to_binary(decimal_number)
print(f'{decimal_number} ở dạng nhị phân: {binary_representation}')



#00010001100001010110000111011100 : +
#11011011011110111101101101100010 : key
#11001010111111101011101010111110 : =