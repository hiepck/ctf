#!/usr/bin/python3

from pwn import *

p = remote('35.200.129.176', 1337)

p.interactive()