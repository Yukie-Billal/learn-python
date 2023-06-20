# Global & local Scopes

g_nama = "Yukie" # Global variabel

def cetak() :
    l_nama = "Billal" # local variabel
    print(f"Nama saya adalah {g_nama}")

# print(l_nama)

for x in range(5) :
    print(f"{x} - {g_nama}")
    
if True :
    print(f'if menampilkan {g_nama}')
    
    
def say_yukie() :
    print(nama)
    
# say_yukie()
nama = "Yukie"
say_yukie()


count = 0 # <- Global Scope

def add() :
    # count = 1 # <- Its will be a local scope variable
    global count # <- FUNGSI ini dapat merubah global variabel
    count = 1

print(f"Sebelum : {count}")
add()
print(f"Sesudah : {count}")

for i in range(5) :
    count += i # <- its a Global Scope Variable, Be carefull
print(f"Sesudah for : {count}")

if True :
    count = 1 # <- Same like for statement
print(f"Sesudah if : {count}")
