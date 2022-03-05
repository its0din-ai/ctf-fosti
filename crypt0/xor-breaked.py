#!/usr/bin/env python3

from random import randint
from base64 import b64encode, b64decode

def xor(string, key):
	return ''.join(chr(ord(i)^key) for i in string)

if __name__ == '__main__':
	flagen	= "Ayo2MSwGEQM+BzcgJC4aHSo3GgArJjc8NTEsKis4"
	flag	= b64decode(flagen).decode()
	key		= 69		# Dapet key dari Bruteforce
	enc		= b64encode(xor(flag, key).encode()).decode()
	breaking = b64decode(enc).decode()

	print("[*] Enc:", breaking)
	print("[*] Key:", key)

"""
Output:	
[*] Enc: Ayo2MSwGEQM+BzcgJC4aHSo3GgArJjc8NTEsKis4
[*] Key: <REDACTED>
"""