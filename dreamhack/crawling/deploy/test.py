from urllib.parse import urlparse
from re import split
import socket
import requests
import ipaddress
from urllib.parse import urlparse
from flask import Flask, request, render_template

def lookup(url):
    try:
        return socket.gethostbyname(url)
    except:
        return False

def check_global(ip):
    try:
        return (ipaddress.ip_address(ip)).is_global
    except:
        return False

def check_get(url):
    ip = lookup(urlparse(url).netloc.split(':')[0])
    if ip == False or ip =='0.0.0.0':
        return "Not a valid URL."
    res=requests.get(url)
    if check_global(ip) == False:
        return "Can you access my admin page~?"
    for i in res.text.split('>'):
        if 'referer' in i:
            ref_host = urlparse(res.headers.get('refer')).netloc.split(':')[0]
            if ref_host == 'localhost':
                return False
            if ref_host == '127.0.0.1':
                return False 
    res=requests.get(url)
    return res.text

url = 'http://localhost'

ip = lookup(urlparse(url).netloc.split(':')[0])
print(ip)