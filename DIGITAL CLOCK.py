# Digital Clock using PYTHON

import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    window.after(1000, update_time)

window = tk.Tk()
window.title('Digital Clock')

label = tk.Label(window, font=('Arial', 80), bg='white', fg='black')
label.pack(padx=50, pady=50)

update_time()

window.mainloop()
