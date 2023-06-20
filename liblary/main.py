import datetime

time = datetime.datetime.now()
print(f"Data Waktu : {time}")
print(f"Data Tahun : {time.year}")
print(f"Data Hari : {time.strftime('%A')}")


from collections import Counter

data = ["a","b","g","a","o","c","b","a"]
data_count = Counter(data)

print(f"Data counter : {data_count}")
print(f"Jumlah a : {data_count['a']}")

import io 

'''BE CAREFULL - method open mengambil directory berdasarkan dimana program dijalankan.
Contoh :
 - main.py berada dalam folder liblary
 - Tetapi dijalankan dengan cara `python liblary/main.py`
 - Maka akan dilakukan pengecekan file `diluar directory liblary`
 
 - Jika ingin dilakukan pengecekan berdasarkan directory dimana main.py berada
 - Maka lakukan `cd liblary` atau masuk dalam dir liblary
'''
file_text = io.open("text.txt","r")
print(file_text.read())