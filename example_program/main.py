from random import random;

number = round(random() * 10)
print("TEBAK ANGKA 1 - 10")
value = int(input("Masukkan Angka Pilihan mu : "))
while value:
	if value > number:
		print("Pilihan anda terlalu besar")
		value = int(input("Tebak Lagi : "))
	elif value < number:
		print("Pilihan anda terlalu kecil")
		value = int(input("Tebak Lagi : "))
	elif value == number:
		print("Selamat Pilihan anda benar")
		break
	
