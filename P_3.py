import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

def show_summary():
    judul = judul_entry.get()
    pengarang = pengarang_entry.get()
    tipe_buku = tipe_var.get()
    tanggal = tanggal_var.get()
    bulan = bulan_var.get()
    tahun = tahun_var.get()
    summary = (f"Judul Buku: {judul}\nPengarang: {pengarang}\nTipe Buku: {tipe_buku}\nTanggal Terbit: {tanggal}/{bulan}/{tahun}")
    messagebox.showinfo("Summary Data Buku", summary)

root = tk.Tk()
root.title("Form Input Data Buku")

window_width = 420
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

fontStyle = tkFont.Font(family="Lucida Grande", size=12)

logo_image = tk.PhotoImage(file="book_logo.png")
logo_image = logo_image.subsample(30, 30) # Mengurangi ukuran gambar

judul_form = ttk.Label(root, text="Form Input Data Buku", font=("Lucida Grande", 14, 
"bold"))
judul_form.grid(row=0, column=0, columnspan=4, pady=(10,0))

logo_label = ttk.Label(root, image=logo_image)
logo_label.grid(row=1, column=0, columnspan=4, pady=(5,10))

separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=2, column=0, columnspan=4, sticky='ew', padx=5, pady=5)

# Membuat dan menempatkan widget dengan grid
judul_label = ttk.Label(root, text="Judul Buku:", font=fontStyle)
judul_label.grid(row=3, column=0, sticky='e', padx=5, pady=2)

judul_entry = ttk.Entry(root, font=fontStyle)
judul_entry.grid(row=3, column=1, columnspan=3, sticky='we', padx=5, pady=2)

pengarang_label = ttk.Label(root, text="Nama Pengarang:", font=fontStyle)
pengarang_label.grid(row=4, column=0, sticky='e', padx=5, pady=2)
pengarang_entry = ttk.Entry(root, font=fontStyle)
pengarang_entry.grid(row=4, column=1, columnspan=3, sticky='we', padx=5, pady=2)

tipe_label = ttk.Label(root, text="Tipe Buku:", font=fontStyle)
tipe_label.grid(row=5, column=0, sticky='e', padx=5, pady=2)
tipe_var = tk.StringVar()

tipe_combobox = ttk.Combobox(root, textvariable=tipe_var, font=fontStyle, state="readonly")
tipe_combobox['values'] = ('buku cerita', 'buku pelajaran', 'buku pengetahuan umum')
tipe_combobox.grid(row=5, column=1, columnspan=3, sticky='we', padx=5, pady=2)

tanggal_label = ttk.Label(root, text="Tanggal Terbit:", font=fontStyle)
tanggal_label.grid(row=6, column=0, sticky='e', padx=5, pady=2)

tanggal_var = tk.StringVar()
bulan_var = tk.StringVar()
tahun_var = tk.StringVar()

tanggal = ttk.Combobox(root, textvariable=tanggal_var, font=fontStyle, state="readonly", 
width=5)
tanggal['values'] = [str(i) for i in range(1, 32)] # 1 sampai 31
tanggal.grid(row=6, column=1, sticky='we', padx=(5, 0), pady=2)

bulan = ttk.Combobox(root, textvariable=bulan_var, font=fontStyle, state="readonly", 
width=8)
bulan['values'] = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] # 12 Bulan
bulan.grid(row=6, column=2, sticky='we', padx=5, pady=2)
tahun = ttk.Combobox(root, textvariable=tahun_var, font=fontStyle, state="readonly", 
width=7)

tahun['values'] = [str(i) for i in range(1980, 2025)] # Tahun 1980 sampai 2024
tahun.grid(row=6, column=3, sticky='w', padx=(0, 5), pady=2)
submit_button = ttk.Button(root, text="Submit", command=show_summary)
submit_button.grid(row=7, column=0, columnspan=4, pady=20)

root.mainloop()