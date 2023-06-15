data = ["Yukie","Billal","Fadhil"]

print(data)
print("Data ke [0]",data[0])

print("Panjang", len(data))
data.insert(1, "Asep")
print("insert",data)
data.append("Ujang")
print("apeend",data)

nama_baru = ["Udin", "Ucup", "Galih"]
data.extend(nama_baru)
print("extends",data)

data[-1] = "Yukie"
print("Declarasi",data)

data.remove("Udin")
print("Remove",data)

data.pop()
print("Pop",data)

angka = [1,6,4,5,1,7,8,5,4,1,2,6,7,8,9,5,3,6,4]
print(f"Angka : {angka}")
print(f"Jumlah Angka 4 : {angka.count(4)}")
print(f"Jumlah Angka 3 : {angka.count(3)}")


angka.sort()
print("Sort Angka",angka)
angka.reverse("Reverse angka", angka)

# data_diri = [["Yukie", "Muhammad", "Billal"], 18, "L", 166.5]
nama = ["Yukie", "Billal", "Fadhil"]
print(nama)
print(f"Index Fadhil : {nama.index('Fadhil')}")
print(f"Index Billal : {nama.index('Billal')}")

nama.sort()
print("Sort string", nama)

nama.reverse()
print(f"Reverse string {nama}")


