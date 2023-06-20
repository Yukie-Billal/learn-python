def tambah(*args:float) -> float:
    output = 0
    for i in args :
        output += 1
    return output

def kali(*args:float) -> float :
    output = 1
    for i in args :
        output *= i
    return output
