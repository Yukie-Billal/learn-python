first_name = "Yukie"
middle_name = "M"
last_name = "Billal"

full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

# Length String
print(len(full_name))

# IN
partials = 'uki'
print(partials in full_name)

# NOT IN
print(partials not in full_name)

# Loop string
print("wk"*10)
print(15*"wk")

print('\n------\n')
# string index
print("Index ke fullname[]")
print("[0]",full_name[0])
print("[1]",full_name[1])
print("[6]",full_name[6])
print("[-1]",full_name[-1])
print("[-6]",full_name[-6])
print("\n---- Range")

print("[0:3]",full_name[0:3])
print("[3:13]",full_name[3:14])

print("\n[3:13]",full_name[0:14:2])

# Item paling kecil
print("\n Paling kecil", min(full_name))

# Item paling besar
print("\n Paling besar", max(full_name))


ascii_code = ord(" ")
print("ASCII CODE untuk spasi adalah", str(ascii_code))

data = 117
print("char untuk ASCII", data, "Adalah", chr(data))



# Operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah Huruf o Pada", data ,"Adalah ",jumlah)