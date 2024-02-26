# TUTORIAL BY WEB PROGRAMMING UNPAS - SANDHIKA GALIH

import tkinter as tk
from tkinter import ttk # theme tkinter
from tkinter.messagebox import showinfo

# window adalah object, configure adalah methodnya
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

# FRAME INPUT
input_frame = ttk.Frame(window)

# PENEMPATAN GRID
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

# VARIABEL
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# KOMPONEN
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10,fill="x", expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang")
nama_belakang_label.pack(padx=10,fill="x", expand=True)

# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x", expand=True)

# 5. Tombol
def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    print(NAMA_BELAKANG.get())
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="whazzup!",message=pesan)
    
tombol_sapa = ttk.Button(input_frame, text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x', expand=True,pady=10,padx=10)

window.mainloop()