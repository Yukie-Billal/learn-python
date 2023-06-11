a = 10
print("a =",a)

a += 4
print("a += 4 =", a)

a -= 2
print("a -= 2 =", a)

a *= 4
print("a *= 4 =", a)

a /= 2
print("a /= 2 =", a)



b = 5
print("\nb =", b)
b %= 3
print("b %= 3", b)
b **= 3
print("b **= 3", b)
b //= 3
print("b //= 3", b)

print("\nLogic operator\n")
print("\n---(or | )---")
c = False
print("c =",c)
c |= True
print("c |= True =",c)
c |= False
print("c |= False =",c)


print("\n---(and & )---")
d = True 
print("d =",d)
d &= True
print("d &= True =",d)
d &= False
print("d &= False =",d)

print("\n---(xor ^ )---")
e = True 
print("e =",e)
e ^= False
print("e ^= False =",e)
e ^= True
print("e ^= True =",e)

print("\n---(>>)---")
f = 0b0100
print("f =",format(f,'04b'))
f >>= 2
print("f >>= 2 =",format(f,'04b'))

print("\n---(<<)---")
f = 0b0100
print("f =",format(f,'04b'))
f <<= 1
print("f <<= 1 =",format(f,'04b'))

g = 0b0100
print("\n\ng =",format(g,'04b'))
g >>= 2
print("g >>= 2 =", format(g,'04b'))
g <<= 1
print("g <<= 1 =", format(g,'04b'))