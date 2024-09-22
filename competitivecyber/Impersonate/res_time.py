from datetime import datetime, timedelta
import hashlib

def calculate_server_start_time(formatted_uptime, formatted_current_time):
    # Chuyển đổi formatted_current_time thành đối tượng datetime
    current_time = datetime.strptime(formatted_current_time, '%Y-%m-%d %H:%M:%S')
    print('current_time:', current_time)
    # Chuyển đổi formatted_uptime thành đối tượng timedelta
    hours, minutes, seconds = map(int, formatted_uptime.split(':'))
    uptime = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    print('uptime:', uptime)
    
    # Tính server_start_time
    server_start_time = current_time - uptime
    return server_start_time


def res_time(server_start_time):
    server_start_time = datetime.now()
    server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
    secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
    secret_key = secure_key
    
    return secret_key

# Ví dụ sử dụng
formatted_uptime = '0:03:12'  # Giả sử uptime là 1 giờ 23 phút 45 giây
formatted_current_time = '2024-09-21 09:23:19'
server_start_time = calculate_server_start_time(formatted_uptime, formatted_current_time)
print(res_time(server_start_time))  # Output: 2023-10-01 11:11:11