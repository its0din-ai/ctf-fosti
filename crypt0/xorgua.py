#!/usr/bin/env python3

from random import randint
from base64 import b64encode

def xor(string, key):
	return ''.join(chr(ord(i)^key) for i in string)

if __name__ == '__main__':
	flag	= "yPLKV|kyDGPM`VL`YJQB"
	# key		= randint(0, 256)
	# enc		= xor(flag, key).encode().decode()

	# print("[*] Enc:", enc)
	# print("[*] Key:", key)
for i in range(255):
    enc	= xor(flag, i)
    print(f"Key = {i}")
    print(enc)
    print("\n")


"""
Output:	
[*] Enc: yPLKV|kyDGPM`VL`YJQB
[*] Key: 63
"""