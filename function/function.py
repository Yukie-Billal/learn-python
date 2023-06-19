# The logic same like like javascript, php and more


# template - default
# def function_name(argument):
# 	print("function body")

# template - with default argument
# def function_name( string_argument = 'string' , argument_name):
# 	print(f"Nilai argument : {argument}")

# func call - function_name(argument_name = "set argument")
# this will set second argument value to "set argument" & first argument with they default value

# template - with list argument
# def function_name(list_argument = [12,5,True,'sisa']):
# 	list = list_argument.copy()

# template - with many returns
# def function_name(argument1, argument2):
# 	kali = argument1 * argument2
# 	bagi = argument1 / argument2
# 	tambah = argument1 + argument2
# 	kurang = argument1 - argument2
# 	return kali,bagi,kurang,tambah
	

# function_name()

def printWord( str ):
	print(str)

printWord("Hello World")

first = "Yukie"
last = "Muhammad Billal"

def getName():
	return first + " " + last

print(getName())



def aritmatika(a, b):
	kali = a * b
	bagi = a / b
	tambah = a + b
	kurang = a - b
	return kali, bagi, tambah, kurang

kali,bagi,tambah,kurang = aritmatika(9,3)
print(f"kali : {kali}")
print(f"bagi : {bagi}")
print(f"tambah : {tambah}")
print(f"kurang : {kurang}")


def default(input1=1,input2=2,input3=3,input4=4):
	print(f"Input 1 : {input1}")
	print(f"Input 2 : {input2}")
	print(f"Input 3 : {input3}")
	print(f"Input 4 : {input4}")
	return input1 + input2 + input3 + input4

print(f"hasil : {default(input3=10)}")