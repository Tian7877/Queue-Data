import tkinter as tk

root = tk.Tk()
root.title("Aplikasi sederhana")

def on_click():
    label.config(text="Yamete Kudasai")

label = tk.Label(root, text="Haloo Foreas")
label.pack()
button = tk.Button(root,text="Push Me", command=on_click)
button.pack()

root.mainloop()