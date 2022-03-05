#!/usr/bin/env python3

from random import randint
from base64 import b64encode, b64decode

def xor(string, key):
	return ''.join(chr(ord(i)^key) for i in string)


if __name__ == '__main__':
    flag	= str(input("Isikan enkripsi => "))
    key		= 69
    enc	= b64encode(xor(flag, key).encode()).decode()
    print("[*] Enc:", enc)
    print("[*] Key:", key)
    
    for i in range(255):
        enc	= xor(flag, i)
        print(f"Key = {i}")
        print(enc)
        print("\n")

"""
Output:	
[*] Enc: Ayo2MSwGEQM+BzcgJC4aHSo3GgArJjc8NTEsKis4
[*] Key: <REDACTED>
"""