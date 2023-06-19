from main import data_dict

# get length of dictionary
length_dict = len(data_dict)
print(length_dict)


# check available key on dictionary
# return boolean
key = "string"
# key = "stringa"
checkkey = key in data_dict
print(f"apakah {key} terdapat di data_dict : {checkkey}\n")


# get value from dictionary 
print(f"data_dict['string'] : {data_dict['string']}")

# use .get() method will return none when store the invalid value
print(f"data_dict.get('string') : {data_dict.get('string')}")
print(f"data_dict.get('stringa') : {data_dict.get('stringa')}")

# .get() method can return message when the key is not found on dict
print(f"data_dict.get('strong') : {data_dict.get('strong', 'invalid key')}\n")


# update 
print(data_dict)

data_dict["string"] = "String ini diubah"
print(f"""
Updated dict with data_dict['string'] = ...
{data_dict}
\n""")

data_dict.update({"string":"mengubah value dalam dictionary"})
print("Updated dict with data_dict.update({'key':'value'})\n")
print(f"{data_dict}\n")

# add
data_dict["name"] = "Yukie"
print(f"key name is assign with 'Yukie'")
print(data_dict)

# delete
del data_dict["name"]
print(f"\nmenghapus key dict del data_dict['key']\n{data_dict}")