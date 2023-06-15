kumpulan_angka = [4,6,9,12,5,2,3]
print("\nFor loop dan range\n")
for angka in kumpulan_angka:
	print(f"Angka = {angka}")


kumpulan_peserta = ["Yukie","Billal","Fadhil"]

for nama in kumpulan_peserta:
	print(f"Nama : {nama}")



print(f"Kumpulan angka {kumpulan_angka}")
panjang = len(kumpulan_angka)
for i in range(panjang):
	print(f"angka index ke {i} = {kumpulan_angka[i]}")



print("\nWhile loop\n")

print(f"Kumpulan angka {kumpulan_angka}")
panjang = len(kumpulan_angka)

while i < panjang : 
	print(f"angka index ke {i} = {kumpulan_angka[i]}")
	i += 1

# List comprehension

print("\nList comprehension\n")

data = ["Yukie", 1,2,3,"Billal"]

[print(f"data={i}") for i in data]
print(f"angka : {kumpulan_angka}")
kuadrat = [i**2 for i in kumpulan_angka]
print(f"Kuadrat : {kuadrat}")

# Enumerate
print("\nEnumerate\n")
data = ["Yukie", 1,2,3,"Billal"]

for index,data in enumerate(data):
	print(f"Index = {index}, data = {data}")