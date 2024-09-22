import urllib.request
from urllib.parse import urlparse

url = 'http://zmpcbhoxopn5jx8ghtrlv27vlmrdf43t.oastify.com &@127.0.0.1'
urlparse = urlparse(url)
print(urlparse.hostname)