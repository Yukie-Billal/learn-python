full_name = "Yukie Muhammad Billal"
format_str = f"Hai {full_name}"
print(format_str)

age = 18
format_str = f"Your age is {age}"
print(format_str)

boolean = False
format_str = f"is lower ? {boolean}"
print(format_str)

# Bilangan Bulat
angka = 15
format_str = f"BIlangan bulat = {angka:d}"
print(format_str)

# Bilangan dengan ordo ribuan
angka = 500000000
format_str = f"Bilangan ribuan = {angka:,}"
print(format_str)


# Float
angka = 2005.5837
format_str = f"desimal {angka:.3f}"
print(format_str)

# leading zero
angka = 2005.5837
format_str = f"desimal {angka:010.3f}"
print(format_str)

# minus plus
angka = -10
format_str = f"Minus : {angka:+d}"
print(format_str)
angka = 10 
format_str = f"Plus  : {angka:+d}"
print(format_str)


# format %
persentase = 0.045
format_str = f"Persen {persentase:.2%}"
print(format_str)


harga = 5000 
jumlah = 3
format_str = f"Total : Rp.{harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)

angka = 255
angka_binary = f"Binary : {bin(angka)}"
angka_hex = f"Hexa : {hex(angka)}"
angka_octal = f"Octal : {oct(angka)}"

print(angka)
print(angka_binary)
print(angka_octal)
print(angka_hex)