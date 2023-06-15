from funct import cekGanjil

print("Belajar if elif else statement python")

angka = int(input("Masukkan angka : "))

if angka > 0:
	print(f"{angka} Adalah bilangan bulat")
	ganjil = input("Periksa apakah angka bilangan ganjil (y/n) ")

	if ganjil in ['y','ye','yes']: cekGanjil(angka)
elif angka == 0:
	print(f"{angka} Adalah bilangan 0 / nol / zero")
else :
	print(f"{angka} Adalah bilangan negatif")
