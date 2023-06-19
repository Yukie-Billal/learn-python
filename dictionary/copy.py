from main import data_dict, friends

teman_teman = friends.copy()

print(f"teman teman\t: {teman_teman}")
print(f"friends \t: {friends}")

teman_teman["new"] = "data baru"

print(f"teman teman\t: {teman_teman}")
print(f"friends \t: {friends}\n")

print(f"Data awal \t: {teman_teman}")

# berdasarkan key
data_grey = teman_teman.pop("gre")
print(f"data grey\t: {data_grey}")
print(f"Sesudah \t: {teman_teman}\n")

# item terakhir
data_akhir = teman_teman.popitem()
print(f"data grey\t: {data_akhir}")
print(f"Sesudah \t: {teman_teman}\n")
