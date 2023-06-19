from main import data_dict, friends

print(friends)

for friend in friends:
	print(friend)
print("it will loop the key")


# soo
print("\nwith .keys() method")
for key in friends.keys():
	print(f"key : {key}")
	print(f"value : {friends.get(key)}\n")

print(f"With .values() method\n")
values = friends.values()
print(values)
for value in values:
	print(f"{value}")


items = friends.items()
print(items)

for item in items:
	print(item)

for key,value in friends.items():
	print(f"key : {key}, value : {value}")