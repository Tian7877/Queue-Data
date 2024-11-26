import tkinter as tk 
from tkinter import ttk

class AppGUI:
    def __init__(self,root):
        self.root = root
        self.root.title("Aplikasi Sederhana")
        self.root.geometry("400x200")
        self.root.configure(bg="#ADD8E6")
        self.create_widgets()
    
    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Masukkan Nama anda", background="#ADD8E6",foreground="black")
        self.label.pack(pady=10)
        self.name_entry = ttk.Entry(self.root, font=('Arial',10))
        self.name_entry.pack(pady=5)

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.display_name)
        self.submit_button.pack(pady=10)
        
        self.message_label = ttk.Label(self.root,background="#ADD8E6", foreground="black")
        self.message_label.pack(pady=10)

    def display_name(self):
        name = self.name_entry.get()
        welcome_message =f"Selamat Datang {name}"
        self.message_label.config(text=welcome_message)

if  __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()