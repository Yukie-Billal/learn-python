import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror,showwarning

# Init
window = tk.Tk()
window.configure(bg="#f9f9f9")
window.title("Kalkulator Sederhana")
window.geometry("600x500")
window.resizable(False,False)


# funct and var
NUM1 = tk.StringVar()
NUM2 = tk.StringVar()

def make_button_component(txt:str,callback) :
    component = ttk.Button(main_frame,text=txt,command=callback)
    component.pack(padx=10,pady=10,fill="x",expand=True)

def make_input_label(txt:str) :
    input_label = ttk.Label(main_frame,text=txt)
    input_label.pack(padx=10,pady=3,fill="x",expand=True)

def make_input_entry(var) :
    input_entry = ttk.Entry(main_frame,textvariable=var)
    input_entry.pack(padx=10,pady=3,fill="x",expand=True)

def convert_int(a, b) :
    return int(a), int(b)

def tambah_btn() : 
    num1, num2 = convert_int(NUM1.get(),NUM2.get())
    output = num1 + num2
    print(f"{num1} + {num2} = {output}")
    showinfo(title="HASIL",message=f"{num1} + {num2} = {output}")

def kali_btn() :
    num1, num2 = convert_int(NUM1.get(),NUM2.get())
    output = num1*num2
    print(f"{num1} * {num2} = {output}")
    showinfo(title="HASIL",message=f"{num1} * {num2} = {output}")

def bagi_btn() :
    num1, num2 = convert_int(NUM1.get(),NUM2.get())
    output = num1/num2
    print(f"{num1} / {num2} = {output}")
    showinfo(title="HASIL",message=f"{num1} / {num2} = {output}")
def kurang_btn() :
    num1, num2 = convert_int(NUM1.get(),NUM2.get())
    output = num1-num2
    print(f"{num1} - {num2} = {output}")
    showinfo(title="HASIL",message=f"{num1} - {num2} = {output}")

# frame
main_frame = ttk.Frame(window)
main_frame.pack(padx=100,fill="x",expand=True)

# Component
# 1. Title
title_label = ttk.Label(main_frame,text="Kalkulator Sederhana")
title_label.pack(padx=20,pady=20,fill="x",expand=True)
title_label.configure(font="300px")


# 2. first number
make_input_label("Bilangan Pertama")
make_input_entry(NUM1)

# 3. second number
make_input_label("Bilangan Kedua")
make_input_entry(NUM2)

make_input_label("Pilih Operator")
make_button_component("Tambah ( + )",tambah_btn)
make_button_component("Kurang ( - )",kurang_btn)
make_button_component("Kali ( * )",kali_btn)
make_button_component("Bagi ( / )",bagi_btn)

window.mainloop()