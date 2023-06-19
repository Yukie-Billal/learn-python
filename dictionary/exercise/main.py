import datetime
import os
import random
import string
from funct import display_mhs

# dict template
mahasiswa_template = {
	"nama" : "nama",
	"nim" : '00000',
	"sks_lulus" : 0,
	"lahir" : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system("clear")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
while True:
	print("-"*20)

	mahasiswa = dict.fromkeys(mahasiswa_template.keys())
	mahasiswa["nama"] = input("Masukkan Nama : ")
	mahasiswa["nim"] = input("Masukkan NIM : ")
	mahasiswa["sks_lulus"] = input("Masukkan sks : ")
	YEAR = int(input("Tahun lahir (yyyy) : "))
	MONTH = int(input("Bulan lahir (1-12) : "))
	DAY = int(input("Tanggal lahir (1-31) : "))
	mahasiswa["lahir"] = datetime.datetime(YEAR,MONTH,DAY)

	KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
	data_mahasiswa.update({KEY:mahasiswa})

	display_mhs(data_mahasiswa)
	if input("\nTambah mahasiswa (y/n) ") not in ["y","ye","yes"]:
		break

print("\nTerima kasih !!\n")