from base64 import b64decode, b32decode

def bas32(encode):
    plain = b32decode(encode).decode()
    return str(plain)

def bas64(encode):
    plain = b64decode(encode).decode()
    return str(plain)

encode = str(input("Masukkan Encodingnya: "))
print("[1] Base32   [2] Base64")
pil = str(input("Pilih Encodingnya: ")).lower()

if pil == "1" or "base32":
    print("Hasil Decoding Base32: ", bas32(encode))
elif pil == "2" or "base64":
    print("Hasil Decoding Base64: ", bas64(encode))
else:
    print("Pilihan tidak ada")
print("=============================================================")
print("tengks. Odin")