length = int(input("Masukkan panjang bintang : "))
count = 1
for x in range(length):
	print("*"*count)
	count += 1

print("\nDibalik\n")

count = 0
for x in range(length):
	print("*"*(length - count))
	count += 1

print("\nDisatukan\n")
count = 1
for x in range(length):
	print("*"*count)
	count += 1
count = 0
for x in range(length):
	print("*"*(length - count))
	count += 1

print("\nDengan while\n")
count = 1
while True :
	print("*"*count)
	count += 1
	if count > length : break

print("\nmirror horizontal\n")
count = 1
space = int(length)
for x in range(length):
	print(" "*space,"+"*count)
	count += 1
	space -= 1

print("\nSama kaki\n")

count = 1
space = int(length/2)
for x in range(length):
	if count % 2:
		print(" "*space, "+"*count)
		count += 1
		space -= 1
		continue
	count += 1










