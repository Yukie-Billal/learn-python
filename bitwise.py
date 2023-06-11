a = 9
b = 5 

#  Bitwise OR (|)
c = a or b # deffirent operator and logic
print(c)
print("========OR(|)========")
c = a | b
print("Nilai a :",a,", Binary :", format(a, '08b'))
print("Nilai a :",b,", Binary :", format(b, '08b'))
print("-------------------------(|)")
print("Nilai c :",c,", Binary :", format(c, '08b'))

print("\n========AND(&)========")
c = a & b 
print("Nilai a :",a,", Binary :", format(a, '08b'))
print("Nilai a :",b,", Binary :", format(b, '08b'))
print("-------------------------(&)")
print("Nilai c :",c,", Binary :", format(c, '08b'))

print("\n========XOR(^)========")
c = a ^ b 
print("Nilai a :",a,", Binary :", format(a, '08b'))
print("Nilai a :",b,", Binary :", format(b, '08b'))
print("-------------------------(^)")
print("Nilai c :",c,", Binary :", format(c, '08b'))

print("\n========NOT(~)========")
c = ~a 
print("Nilai a :",a,", Binary :", format(a, '08b'))
print("-------------------------(~)")
print("Nilai c :",c,", Binary :", format(c, '08b'))

# d = 0b0000001001
# e = 0b1111111111
# print("Nilai :", e^d,', Binary :', format(e^d, '08b'))

print("\n========shift right(>>)========")
c = a >> 3 
print("Nilai a :",a,", Binary :", format(a, '08b'))
print("-------------------------(^)")
print("Nilai c :",c,", Binary :", format(c, '08b'))

print("\n========shift left(<<)========")
c = a << 2 
print("Nilai a :",a,", Binary :", format(a, '08b'))
print("-------------------------(^)")
print("Nilai c :",c,", Binary :", format(c, '08b'))

# NOTE counter part nya, mengambil nilai minus / mirror dari nilai hasil nya. 
# Mirror nya dimulai dari nol bagian minus. sehingga jika nilainya +3 maka akan menjadi -4

