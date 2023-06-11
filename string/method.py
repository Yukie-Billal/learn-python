# Method objec string

full_name = "yukie muhammad billal"
# Capitalize
full_name = full_name.capitalize()
print("capital :",full_name)

# upper case
full_name = full_name.upper()
print("upper :",full_name)

# lower case
full_name = full_name.lower()
print("Lower :",full_name)

# pengecekan dengan .is selalu menghasilkan boolean
print("is upper ?",full_name.isupper())
print("is lower ?",full_name.islower())


# isalnum() <-- pengecekan huruf angka
# isdecimal() <-- pengecekan angka / number
# isalpha() <-- pengecekan huruf semua
# isspace() <-- pengecekan spasi, newline, tab - \t \n
# istitle() <-- pengecekan huruf besar setiap kata

print("is title ?",full_name.istitle())
full_name = full_name.title()
print("title :",full_name)
print("is title ?",full_name.istitle())

print("\n")

print("start with",full_name.startswith("Yukie"))
print("end with",full_name.endswith("Billal"))


print("\n")

# Join , split
print(full_name)
full_name = full_name.split(' ')
print("Dipisah :",full_name, " berdasarkan  (spasi)")
print("DI satukan", '-'.join(full_name), "dengan ( - )")



# alokasi karakter rjust() ljust() center()

example = 5*"="+"Data"+"="*5
print("\n",example)

print("Dengan rjust")
text = "Right".rjust(10)
print("-" + text + "-")

print("Dengan ljust")
text = "Left".ljust(10)
print("-" + text + "-")

print("Dengan center")
text = "Center".center(20, '*')
print(text)

#  Kebalikannya

print("-"+text.strip("*")+"-")