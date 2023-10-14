#!/bin/bash

# Tên tệp ZIP ban đầu
initial_zip_file='zip-999.zip'

# Số lần giải nén (25000 lần)
num_extractions=9999

# Thư mục chứa tệp ZIP
zip_folder='.'

# Lệnh bạn muốn thực hiện sau khi giải nén
command_after_extraction='echo "Hello, this is $1"'

for ((i=0; i<num_extractions; i++)); do
  # Tìm tệp password tương ứng với tệp ZIP
  password_file="${zip_folder}/password.txt"
  
  # Kiểm tra xem tệp password tồn tại
  if [ -f "$password_file" ]; then
    # Đọc mật khẩu từ tệp password
    password=$(cat $password_file)
  else
    echo "Lỗi: Tệp password-${i}.txt không tồn tại."
    exit 1
  fi
  cat $password_file
  echo $password_file
  echo $password
  # Giải nén tệp ZIP bằng mật khẩu
  unzip -P $password -o $initial_zip_file -d $zip_folder
  
  # Thực hiện lệnh đã cho
  eval "$command_after_extraction"
  
  # Xoá tệp ZIP cũ
  rm "$initial_zip_file"
  
  # Tạo tên tệp ZIP tiếp theo
  next_index=$((9999 - i - 1))
  initial_zip_file="zip-$(printf '%d' "$next_index").zip"
done
