count = 0

while count < 5 :
	print(f"Nilai : {count}")
	count += 1


count = 0
while True:
	print("Akan selalu dijalankan")
	count += 1
	if count == 4: break

print("Mencetak bilangan genap")
number = 0
while number < 25:
	number += 1
	if number % 2:
		continue
	print(f"Nilai {number}")

print("Mencetak bilangan ganjil")
number = 0
while number < 25:
	number += 1
	if (number % 2) == 0:
		continue
	print(f"Nilai {number}")

if number :
	pass
	print("Finish")