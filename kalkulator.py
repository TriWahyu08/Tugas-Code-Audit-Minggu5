# Kode Legacy (Berantakan)
# Fungsi untuk menghitung
def hitung(a, b, c):
    # menghitung diskon
    d = a * (b / 100)
    res = a - d

    # jika member dapat potongan tambahan 5000
    if c == True:
        res = res - 5000

    print("Total yang harus dibayar: ", res)
    return res

# Transaksi 1
p = 100000
disc = 10
m = True
hitung(p, disc, m) # Panggil fungsi

# Duplikasi (Pelanggaran DRY)
p2 = 200000
disc2 = 15
m2 = False
d2 = p2 * (disc2 / 100)
res2 = p2 - d2
if m2 == True:
    res2 = res2 - 5000
print("Total yang harus dibayar: ", res2)