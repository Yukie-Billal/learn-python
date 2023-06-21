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
    event_button("+")

def kali_btn() :
    event_button("*")

def bagi_btn() :
    event_button("/")
    
def kurang_btn() :
    event_button("-")

def event_button(operator) :
    num1, num2 = convert_int(NUM1.get(),NUM2.get())
    hasil = getOutput(num1,num2, operator)
    showinfo(title="HASIL",message=hasil)
    
def getOutput(num1, num2, operator) :
    if operator =="+":
        return f"Hasil {num1} {operator} {num2} = {num1 + num2}"
    elif operator == "-" :
        return f"Hasil {num1} {operator} {num2} = {num1 - num2}"
    elif operator == "*" :
        return f"Hasil {num1} {operator} {num2} = {num1 * num2}"
    elif operator == "/" :
        return f"Hasil {num1} {operator} {num2} = {num1 / num2}"
    else :
        return f"Input Salah. Silahkan Masukkan sekali lagi.."

button_dict = {
    "Tambah (+)" : tambah_btn,
    "kurang (-)" : kurang_btn,
    "kali (*)" : kali_btn,
    "bagi (/)" : bagi_btn
}

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

for item in button_dict.items() :
    make_button_component(item[0],item[1])

window.mainloop()