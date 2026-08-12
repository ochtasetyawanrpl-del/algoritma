#  Input
nama = input("Masukkan nama: ")

# Aritmatika (+ dan /)
nilai = 80 + 10  # Hasil = 90
rata2 = nilai / 1 # Hasil = 90.0

#  Perbandingan (>= dan ==) & 4. Logika (and, or)
lulus = (rata2 >= 70) and (nilai == 90)   # True and True -> True
juara = (rata2 > 80) or (nilai < 50)     # True or False -> True

# Output (Hasil True Semua)
print("Siswa:", nama)
print("Lulus?", lulus) # True
print("Juara?", juara) # True

