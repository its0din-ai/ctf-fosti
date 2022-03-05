
biner = str(input("Masukkan biner: "))

bins = biner.split()
plainTek = ""

for xxx in bins:
    integ = int(xxx, 2)
    asciiiiiii = chr(integ)
    plainTek += asciiiiiii

print("\n===========================================================================================")
print("Liat Hasilnya Boss! => ", plainTek)
print("===========================================================================================")