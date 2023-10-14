import zipfile
import os

# Mật khẩu ban đầu từ tệp password.txt

# Số lần giải nén (10 lần)
num_decryptions = 25000

# Tên tệp ZIP ban đầu
original_zip_file = "zip-25000.zip"
check_num = 1
for i in range(num_decryptions, 0, -1):
    with open("password.txt", "r") as password_file:
        password = password_file.read().strip()
    # Tạo tên tệp ZIP mới với số thứ tự (ví dụ: zip-24998.zip, zip-24997.zip, ...)
    new_zip_file = f"zip-{25000 - check_num}.zip"

    # Đổi mật khẩu mỗi lần giải nén

    # Thử giải nén tệp ZIP với mật khẩu
    try:
        with zipfile.ZipFile(original_zip_file, 'r') as zip_ref:
            zip_ref.extractall(pwd=password.encode('utf-8'))
        #print(f"Giải nén lần {i} thành công.")
    except zipfile.BadZipFile:
        print(f"Lỗi: Lần {i} - Đây không phải là tệp ZIP hợp lệ.")
    except RuntimeError as e:
        print(f"Lỗi: Lần {i} - Mật khẩu không đúng.")
    except Exception as e:
        print(f"Lỗi: Lần {i} - {str(e)}")

    # Xoá tệp ZIP ban đầu
    os.remove(original_zip_file)

    # Đổi tên tệp ZIP mới thành tên tệp ZIP ban đầu
    original_zip_file = new_zip_file

    check_num += 1