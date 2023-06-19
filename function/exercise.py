import os


def header():
	print(f"{'MENGHITUNG LUAS DAN':^40}")
	print(f"{'KELILING PERSEGI PANJANG':^40}")
	print('-'*40)

	print("""
Menu :
 - Keliling (k)
 - Luas (l)
		""")

def input_user():
	menu = input("Pilihan menu : (k/l) ")
	lebar = int(input("Masukkan nilai lebar\t: "))
	panjang = int(input("Masukkan nilai panjang\t: "))
	return menu, lebar, panjang

def hitung_luas(lebar, panjang):
	return lebar * panjang

def hitung_keliling(lebar, panjang):
	return 2*(panjang+lebar)

def show(message, value):
	print(f"{message} persegi panjang adalah : {value}")

while True :
	os.system("clear")
	header()

	menu, lebar, panjang = input_user()
	if menu not in ["k","l","K","L"]:
		print("Silahkan Pilih menu yang tersedia")
		break

	if menu in ["l","L"]:
		luas = hitung_luas(lebar, panjang)
		show("Luas", luas)
	else:
		keliling = hitung_keliling(lebar, panjang)
		show("Keliling", keliling)
		pass
	
	if input("Ulangi ? (y/n) ") not in ["y","ye","yes"]:
		break
