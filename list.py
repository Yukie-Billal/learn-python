# FOR NOTE list is array in javascript

list1 = ["Yukie","Muhammad","Billal"]
list2 = ["Yukie", 18, '2004', 165.5 , False]
list3 = ["Y", "U", "K", "I", "E"]

list2[2] = '1990'

print("List1[0] :", list1[0])
print("List2[4] :", list2[1:4]) # The [ : ] method is return list type again

print([1,3,5,7][1:5])

del list3[0]
del list3[3]
print(list3)

if len(list3) >= 0:
	print("Panjang list / length =",len(list3))
	list3 += ["B","I","L","L","A","L"]
	print("List now :",list3)

	print(['Hai'] * 4)

print("U" in list3)