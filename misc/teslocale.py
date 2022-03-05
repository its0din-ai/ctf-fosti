import math
from decimal import ROUND_DOWN

angka1 = 84
angka2 = 39

hasil = angka1 / angka2

zzz = math.floor(hasil * 10 ** 1) / 10 ** 1
hasilul = str(zzz).replace('.', ',')

print(hasilul)