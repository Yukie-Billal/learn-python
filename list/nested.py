peserta_1 = ["Yukie", 18, "L"]
peserta_2 = ["Amel", 17, "P"]
peserta_3 = ["Fadhil", 13, "L"]


list_peserta = [peserta_1, peserta_2, peserta_3]
print(list_peserta)

for peserta in list_peserta:
	print(f"Nama\t: {peserta[0]}")
	print(f"Umur\t: {peserta[1]}")
	print(f"Gender\t: {peserta[2]}\n")


list_copy = list_peserta.copy()
print(list_copy)

peserta_1[0] = "Billal"
print("Copy : ", list_copy)
print("list peserta : ", list_peserta)