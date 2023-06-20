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
        

        
        
    
aritmatika(1,2,3,4,5,6, operator="tambah")
