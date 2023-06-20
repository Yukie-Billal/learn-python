# Template
# import tambah
# from tambah import tambah as add
# import sains.matematika
# from sains import matematika as mtk
# from sains.matematika import kali as k


# Case

import tambah
from tambah import tambah as add

hasil = tambah.tambah(5,5)
print(f"Hasil : {hasil}")

hasil = add(6,6)
print(f"Hasil : {hasil}")




# PACKAGE
# import sains
import sains.matematika

hasil_sains = sains.matematika.kali(5,5)
print(f"Hasil sains matematika kali = {hasil_sains}")


from sains import matematika as mtk
hasil_mtk = mtk.kali(2,2,2)
print(f"Hasil mtk kali = {hasil_mtk}")

from sains.matematika import kali as k

hasil_kali = k(8,8)
print(f"Hasil Kali = {hasil_kali}")