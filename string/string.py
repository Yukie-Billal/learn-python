# my_text = """this is a long string that is made up of
# several lines and non-printable characters such as
# TAB ( \t ) and they will show up that way when displayed.
# NEWLINEs within the string, whether explicitly given like
# this within the brackets [ \n ], or just a NEWLINE within
# the variable assignment will also show up.
# """
# print (my_text)

# first = "Yukie"
# last = "Billal"

# print("first[0]", first[0])
# print("last[1:4]", last[1:4])

# my_string = "Hello World"
# print("Update string :", my_string)
# new_string = input("Masukkan String baru : ")
# my_string = my_string[:6] + new_string
# print("String baru anda :", my_string)

# print("This is first line \nAnd this is a second line \t \\t is tab and \\n is newline. multiline in one line syntax")

# print(first in last)
# print("Yu" in first)
# print("B" in last)

def newline():
	print("\n")

my_name = "Yukie muhammad Billal"

string = "Ini adalah string"
print(string)
print(type(string),"\n\n")

'''
	1. Dengan single quote '...'
	2. Dengan double quote "..."
	3. Nesting quote
	4. nested with backslash
	5. Backslash method list
'''

# 1
string = 'String single quote\n'
print(string)

# 2
string = "String double quote\n"
print(string)

# 3
string = "'Hallo apa kabar?"
print(string)
string = "Ini adalah hari jum'at"
print(string)


# 4 backslash
string = 'Mari Sholat Jum\'at\n'
print(string)

string = "C:\\USER\\Yukie Dev\n"
print(string)


#5 Backslash List

# Tab
print("Saya \tYukie")

# backspace
print("Yukie \bBillal")

newline()
# newline
print("Baris Pertama.\nBaris Kedua.") # LF -> line feed -> untuk unix (mac os, linux)
print("Baris Pertama.\rBaris Kedua.") # CR -> carriage return -> commodore -> acord -> lisp
print("Baris Pertama.\r\nBaris Kedua.") # CRLF -> line feed carriage return -> windows

newline()

# 6 String literal - raw
print("C:\new folder")

print(r"C:\new folder\n\t Not changed")

# newline()

# Multi line
print("""
Nama : Yukie Muhammad Billal
Umur : 18 Tahun
""")

# multi line raw
print(r"""
Nama : Yukie
path : C:\USER\Yukie Dev
""")