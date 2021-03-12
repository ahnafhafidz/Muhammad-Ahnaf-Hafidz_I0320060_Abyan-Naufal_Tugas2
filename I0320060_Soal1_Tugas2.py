print(Praktikum Programa Komputer week 2)

print(Soal 1)

import math

#menampilkan informasi program
print("1. Menghitung Luas Persegi Panjang")

#input nilai panjang dan lebar
p = float(input("Masukkan Nilai Panjang: "))
l = float(input("Masukkan Nilai Lebar: "))

#menghitung luas persegi panjang
luas_persegi_panjang = p * l

#menampilkan hasil perhitungan
print("Luas Persegi Panjang: ", luas_persegi_panjang)


#menampilkan informasi program
print("2. Menghitung Luas Lingkaran")

#input nilai jari-jari
r = float(input("Masukkan nilai jari-jari: "))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)

#menampilkan hasil perhitungan
print("luas lingkaran: ", luas_lingkaran)


#menampilkan informasi program
print("3. Mengitung Luas Permukaan Kubus")

#input nilai sisi kubus
s = float(input("Masukkan Nilai Sisi: "))

#menghitung luas permukaan kubus
luas_kubus = 6 * (s ** 2)

#menampilkan luas permukaan kubus
print("Luas Permukaan Kubus: ", luas_kubus)


#menampilkan informasi program
print("4. Menghitung Konversi Suhu (Celcius ke Fahrenheit)")

#input suhu dalam celcius
C = float(input("Masukkan Suhu dalam Celcius: "))

#menghitung konversi suhu celcius ke fahrenheit
F = 9 * (C + 32) / 5

#menampilkan hasil konversi
print("Celcius: ", C)
print("Fahrenheit: ", F)


#menampilkan informasi program
print("5. Menghitung Konversi Suhu (Reamur ke Kelvin)")

#input suhu dalam reamur
R = float(input("Masukkan Suhu dalam Reamur"))

#menghitung konversi suhu reamur ke kelvin
K = (5 * R / 4) + 273

#menampilkan hasil konversi
print("Reamur: ", R)
print("Kelvin: ", K)
