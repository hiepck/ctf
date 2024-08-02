st = ['1', '_', 'c', '_', '3', '_', 'c', '_', '0', '_', '_', 'f', 'f', '_', '3', 'e']

# Chuyển đổi ngược `st` thành `res`
res_list = []
for char in st:
    if char == '_':
        res_list.append(11)  # `_` tương ứng với 11
    elif char.isdigit():
        res_list.append(int(char))
    else:
        res_list.append(int(char, 16))  # giá trị thập lục phân

# Xây dựng lại giá trị `org`
org = 0
for i, res in enumerate(res_list):
    org |= (res << (4 * (15 - i)))

print(f"Giá trị ban đầu của org: {org}")
