from pwn import *
import math
import datetime


def paksa():
    host 		= "20.106.136.165"
    port 		= "6969"

    HOUR        = datetime.datetime.now().hour
    MINUTE      = datetime.datetime.now().minute
    SECONDS     = datetime.datetime.now().second

    n = 1
    print("====================================================")
    conn = remote(host, port)
    while n>0:
        nn = 1
        try:
            # AMBIL SOAL
            resp = conn.recvline()
            print(f"Soal {n} => " + resp.decode())

            decoded = resp.decode()
            kata = decoded.split()
            angka1 = int(kata[1])
            operator = kata[2]
            angka2 = int(kata[3].strip(":"))

            # AMBIL LEMBAR JAWABAN
            resp1 = conn.recvuntil(b":")
            print(resp1.decode())

            if operator == "-":
                kalkul = angka1 - angka2
                print(f"[DEBUG {n}] {angka1} - {angka2} = {kalkul}")
                # TEORI PERTAMA, KALO HASIL -, KALKULASI GW BALIK
                # TEORI KEDUA, KALO HASIL - GW ILANGIN -NYA [BELUM]

                # if angka1 < angka2:
                #     kalkul = angka2 - angka1
                #     print(f"[DEBUG {n}] {angka1} - {angka2} = {kalkul}")
                # else:
                #     kalkul = angka1 - angka2
                #     print(f"[DEBUG {n}] {angka1} - {angka2} = {kalkul}")
            elif operator == "*":
                kalkul = angka1 * angka2
                print(f"[DEBUG {n}] {angka1} * {angka2} = {kalkul}")
            elif operator == "+":
                kalkul = angka1 + angka2
                print(f"[DEBUG {n}] {angka1} + {angka2} = {kalkul}")
            elif operator == "/":
                # TEORI KETIGA, KALO > NOMOR 1, BALIKIN, FORMAT A.B
                axz = angka1 / angka2
                zzz = math.floor(axz * 10 ** 1) / 10 ** 1
                kalkul = str(zzz).replace('.', ',')
                print(f"[DEBUG {n}] {angka1} / {angka2} = {kalkul}")

            # KUMPULKAN JAWABAN
            conn.send(str(kalkul).encode())

            # # CEK NILAI
            conn.sendline(b"\n")
            resp1 = conn.recvline()
            print(f"==========[{HOUR}:{MINUTE}:{SECONDS}]==========")
            print(f"NILAI SOAL [{n}]=> " + resp1.decode())

            # Masukkan Nilai
            hasil = open("hasil1.txt", "a")
            hasil.writelines(f"[{HOUR}:{MINUTE}:{SECONDS}]   [{n}]  {resp1.decode()}")
            hasil.close()

            # KASIH TAU DI LOG
            fil = open("log.txt", "w")
            fil.writelines(f"\nInisiasi Ke- {nn}")
            fil.close()

            fil = open("log.txt", "a")
            fil.writelines(f"\nPercobaan Ke {n}")
            fil.writelines("\n")
            fil.writelines(resp1.decode())
            fil.close()


            conn.send(b"\n")
            n += 1

        except EOFError:
            print("[!] WRONGG!!!!!")
            fil = open("log.txt", "a")
            fil.writelines("\n")
            fil.writelines(f"Percobaan Ke {n} GAGAL")
            fil.close()

            hasil = open("hasil1.txt", "a")
            hasil.writelines("[>>] Gagal NGABBB!!===========================\n")
            hasil.close()


            conn.close()
            nn += 1
            paksa()

    

paksa()
    # conn.sendline("\n".encode())




# LOOOOPINGGG
# Looping manual jg gpp,
# Loop terus sampe error EOF
# setelah itu ganti delimiter pake } buat dapetin FLAG
#  EEEZZZZZZZ





