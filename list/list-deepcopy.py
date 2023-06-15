data = [[1, 5], [2,4], 10]

data_copy = data.copy()

print(f"Data asli : {data}")
print(f"Data copy : {data_copy}")

print(f"Address asli : {hex(id(data))}")
print(f"Address copy : {hex(id(data_copy))}")

print("Adress nested list ke - 1")
print(f"Address asli : {hex(id(data[0]))}")
print(f"Address copy : {hex(id(data_copy[0]))}")

# data[0][0] = 14
# data[2] = 400
# print("===Diubah===")
# print(f"Data asli : {data}")
# print(f"Data copy : {data_copy}")

from copy import deepcopy
print("\nDeep Copy\n")

data_deepcopy = deepcopy(data)

print(f"Address asli : {hex(id(data))}")
print(f"Address deep : {hex(id(data_deepcopy))}")

print("Adress nested list ke - 1")
print(f"Address asli : {hex(id(data[0]))}")
print(f"Address deep : {hex(id(data_deepcopy[0]))}")

data[0][0] = 14
data[2] = 400
print("===Diubah===")
print(f"Data asli : {data}")
print(f"Data copy : {data_copy}")
print(f"Data deepcopy : {data_deepcopy}")
