import os


# Global variabel
NUM1 = 0
NUM2 = 0

# function
def tambah() :
    return NUM1 + NUM2

def update_display(message) :
    print('-'*30)
    print(f"\n{message}\n")
    print('-'*30,)
    
def header() :
    print(f"{'Kalkulator Sederhana':^40}")
    print(f"{'-'*40:^40}\n")

def input_user(condition:bool = False) :
    global NUM1, NUM2
    if condition :
        print(f"Masukkan Bilangan pertama : {NUM1}") 
        print(f"Masukkan Bilangan kedua : {NUM2}") 
        print(f"\nHarap Untuk memasukkan pilihan yang tersedia!\n")
    else :
        NUM1 = int(input("Masukkan Bilangan pertama : "))
        NUM2 = int(input("Masukkan Bilangan kedua : "))

def getOperator() -> bool:
    print(f"\nDaftar Operator\n - Kali (*) \n - Bagi (/) \n - Tambah (+) \n - Kurang (-) \n{'-'*20}")
    operator = input("Pilih Operator : ")
    if operator in ["+","-","*","/"] : return operator
    return ''

def math(operator:str) -> int:
    if operator == "+" :
        output = NUM1 + NUM2
        return output, f"Hasil dari {NUM1} {operator} {NUM2} = {output}"
    elif operator == "-" :
        output = NUM1 - NUM2
        return output, f"Hasil dari {NUM1} {operator} {NUM2} = {output}"
    elif operator == "*" :
        output = NUM1 * NUM2
        return output, f"Hasil dari {NUM1} {operator} {NUM2} = {output}"
    elif operator == "/" :
        output = NUM1 / NUM2
        return output, f"Hasil dari {NUM1} {operator} {NUM2} = {output}"
    else :
        os.system("clear")
        return 0

while True :
    os.system("clear")
    header()
    if NUM2:
        input_user(True)
    else :
        input_user()
    
    operator = getOperator()
    if operator == '' :
        continue
    hasil, message = math(operator)
    update_display(message)
    
    if input("Ulangi ? (y/n) ") not in ['y',"Y","Ye","ye","yes","Yes"] :
        break
