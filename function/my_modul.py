'''FUNGSI DENGAN HINT'''
def my(argument:int) -> int :
    '''Tipe Hint pada function'''
    return argument**2

print(my(4))

'''FUNGSI DENGAN *args'''
def count(*args:int) -> int:
    output = 0
    for x in args :
        output += x
    return output

print(count(1,2,3))

'''FUNGSI DENGAN KWARGS'''
# NOTE : harus mengirimkan key nya
def describe(**kwargs):
    '''FUNGSI DENGAN KWARGS <-  Bebas dalam hal penamaan
    Akan menghasilkan dictionary
    '''
    for item in kwargs.items():
        print(f"key : {item[0]}, Value : {item[1]}")

describe(nama="Yukie",umur=18)


def aritmatika(*nums:int, **operator) -> int: 
    output =0
    if operator['operator'] in ["tambah","Tambah"]:
        for num in nums :
            output += num
        return output
    elif operator['operator'] in ["Kurang","kurang"]:
        for num in nums :
            output -= num
        return output
    elif operator['operator'] in ["Kali","kali"]:
        output = 1
        for num in nums :
            output *= num
        return output
    elif operator['operator'] in ["Bagi","bagi"]: 
        output = nums[0]
        for num in nums :
            output /= num
        return output
    else :
        return 0

print(aritmatika(1,2,3,4,operator="kali"))


#  LAMBDA FUNCTION
def f_kuadrat(angka:int) ->int :
    return angka**2

print(f"hasil fungsi kuadrat : {f_kuadrat(3)}")

kuadrat = lambda angka: angka**2
print(f"hasil lambda kuadrat : {kuadrat(3)}")

kuadrat = lambda angka,pow: angka**pow
print(f"hasil lambda kuadrat #2 : {kuadrat(3,3)}")


# case - list sort
data_list = ["Yukie","Dudung", "Asep"]
data_list.sort()
print(data_list)

# sort berdasarkan panjang
data_list.sort(key=len)
print(data_list)

data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda : {data_list}")


data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka) :
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(data_angka_baru)
# kasus genap

data_angka_baru = list(filter(lambda x:x<5, data_angka))
print(f"Filter dengan lambda : {data_angka_baru}")


data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(f"Data genap lambda : {data_genap}")

data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(f"Data ganjil lambda : {data_ganjil}")

data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(f"Data kelipatan 3 lambda : {data_3}")

data_4 = list(filter(lambda x:(x%4==0),data_angka))
print(f"Data kelipatan 4 lambda : {data_4}")



# Anonymous function
# currying <- haskel Curry
print(f"\nAnonymous")
def pangkat(angka,n) :
    return angka**n 

print(pangkat(5,2))

def pangkat(n) :
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Pangkat 2 : {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"Pangkat 3 : {pangkat3(5)}")
print(f"Pangkat bebas : {pangkat(4)(5)}")