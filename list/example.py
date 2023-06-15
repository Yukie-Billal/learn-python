print("Program pencatatan data buku sederhana")
list_buku = []
while True:
	judul = input("Judul buku : ")
	penulis = input("Penulis buku : ")

	buku = [judul,penulis]
	list_buku.append(buku)

	print("\n","="*10,"List Buku","\n")
	for i,buku in enumerate(list_buku):
		print(f"{i+1}. {buku[0]} | {buku[1]}")

	print("\n","="*20,"\n")
	if input("Lanjutkan (y/n) ") in ["n","no","nope","nop"]:
		break

print("Program selesai")
