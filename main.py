print("--Contoh Pengkodisian--")
nilai = int(input("Masukkan Nilai : "))
if nilai >= 7:
	print("Selamat anda lulus")
else:
	print("mohon maaf, anda tidak lulus")

print("--Aritmatika--")

first = int(input("Masukkan angka pertama : "))

second = int(input("Masukkan angka kedua : "))
print("Daftar Operator :")
print("**	-	Pangkat")
print("*	-	Perkaliam")
print("/	-	Pembagian")
print("%	-	Modulus")
print("//	-	Floor division")
print("-	-	Pengurangan")
print("+	-	Pemjumlahan")
operator = input("Masukkan Operaor : ")

if operator == '**':
	print("Hasilnya Adalah :",first, operator, second,"=", (first ** second))
elif operator == "*":
	print("Hasilnya Adalah :",first, operator, second,"=", (first * second))
elif operator == "/":
	print("Hasilnya Adalah :",first, operator, second,"=", (first / second))
elif operator == "%":
	print("Hasilnya Adalah :",first, operator, second,"=", (first % second))
elif operator == "//":
	print("Hasilnya Adalah :",first, operator, second,"=", (first // second))
elif operator == "+":
	print("Hasilnya Adalah :",first, operator, second,"=", (first + second))
elif operator == "-":
	print("Hasilnya Adalah :",first, operator, second,"=", (first - second))


print("--Looping--")
print("--While ")
count = int(input("Masukkan angka antara 1 - 10 : "))
while count > 0:
	print("Ini adalah hitungan ke :",count)
	count -= 1

print("--For loop")
angka = [1,2,3,4,5]
print("Contoh bilangan : ",angka)

for x in angka:
	print("Ini adalah", x)

buah = ["nanas", "apel", "semangka"]
print("Contoh Buah :",buah)
for makanan in buah:
	print("Makanan :", makanan)

Contoh penggunaan Nested Loop
Catatan: Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai True(benar) dan nol sebagai False(salah)

# i = 2
# while(i < 10):
# 	j = 2
# while(j <= (i/j)):
# 	if not(i%j): break
# 	j = j + 1
# 	if (j > i/j) : 
# 		print(i, " is prime")
# 		i = i + 1

# print("Good bye!")