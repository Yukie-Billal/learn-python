a = ["Yukie", "Billal", "Fadhil"]
print("a",a)
b = a
print("b",b)


# Ubah
a[-1] = "Zaelani"

print("a",a)
print("b",b)

b[-1] = "Yukie"

print("a",a)
print("b",b)

print(f"address a : {hex(id(a))}")
print(f"address b : {hex(id(b))}")


# Copy list
c = a.copy()
print(f"Copy list dengan .copy : {c}")
print(f"address a : {hex(id(a))}")
print(f"address b : {hex(id(b))}")
print(f"address c : {hex(id(c))}")

print("a",a)
print("b",b)
print("c",c)

print("Ubah c")
c[0] = "Suep"

print("a",a)
print("b",b)
print("c",c)
