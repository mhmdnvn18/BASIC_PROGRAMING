# Output teks ke layar
print("Halo, dunia!")

# Variabel dan tipe data
angka = 10  # Tipe data integer
angka_desimal = 3.14  # Tipe data floating-point
karakter = 'A'  # Tipe data karakter
benar = True  # Tipe data boolean

# Operasi matematika
hasil_penjumlahan = 5 + 3
hasil_pengurangan = 5 - 3
hasil_perkalian = 5 * 3
hasil_pembagian = 6 / 3
sisa_pembagian = 7 % 3

# Percabangan if-else
if angka > 0:
    print("Angka positif")
elif angka < 0:
    print("Angka negatif")
else:
    print("Angka nol")

# Perulangan while
i = 0
while i < 5:
    print("Nilai i:", i)
    i += 1

# Perulangan for
for j in range(5):
    print("Nilai j:", j)

# Tipe Data List (analog dengan Array di C++)
arr = [1, 2, 3, 4, 5]

# Menggunakan tipe data list
print("Elemen-elemen dalam list:")
for elem in arr:
    print(elem)

# Tipe Data Tuple (serupa dengan std::array di C++)
floatArr = (3.14, 2.718, 1.618)

# Menggunakan tipe data tuple
print("Elemen-elemen dalam tuple:")
for elem in floatArr:
    print(elem)

# Tipe Data List (analog dengan std::vector di C++)
vec = [10, 20, 30]

# Menggunakan tipe data list
print("Elemen-elemen dalam list:")
for elem in vec:
    print(elem)
