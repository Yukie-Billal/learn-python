dict = {'Age': 7, 'Class': 'First', "My Name" : "Yukie Muhammad Billal"}

#  NOTE it same like javascript objec. when the object is represented a key and a value. for calling it dict["key name"]
# OR if you know about json. yes the syntax is most like a json with "" inside the key

print ("dict['Name']: ", dict['My Name'])
print ("dict['Age']: ", dict['Age'])


# Don`t forget. it was like a object

dict["Age"] = 18
dict["birthday_year"] = '2004' # create new

print("dict[Age] :", dict["Age"])
print("dict[birthday_year] :", dict["birthday_year"])


del dict["Class"]
print("dictionary value :",dict)
dict.clear()
print("dictionary value :",dict)
del dict


print("dict[birthday_year] : ", dict["birthday_year"])


# some build in dict method 
dict = {'Age': 7, 'Class': 'First', "My Name" : "Yukie Muhammad Billal"}
print(dict.keys()) # see the documentation or some tutorial out there