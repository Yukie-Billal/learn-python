import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

# Variabel & fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def sapa_click() :
    NAMA_DEPAN.set("Text baru yang diubah melalui program")
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Ini Info!",message=pesan)

# Frame input
input_frame = ttk.Frame(window)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=20,fill="x",expand=True)


# Komponen Komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,pady=3,fill="x",expand=True)
# 2. Nama Depan entry
nama_depan_enrty = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_enrty.pack(padx=10,pady=5,fill="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(padx=10,pady=3,fill="x",expand=True)
# 4. Nama belakang entry
nama_belakang_enrty = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_enrty.pack(padx=10,pady=5,fill="x",expand=True)
# 5. Button / Tombol
    
sapa_button = ttk.Button(input_frame,text="Sapa",command=sapa_click)
sapa_button.pack(pady=10,padx=10,fill="x",expand=True)

# Start program
window.mainloop()