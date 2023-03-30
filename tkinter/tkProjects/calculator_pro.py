# This is the best calculator you've ever seen
import tkinter as tk
import ttkbootstrap as ttk

window=ttk.Window()
window.title('Calculator')
window.geometry('400x600')

# FUNCTIONS

# LABEL NUMBERS
frame_label=ttk.Frame(window, width=400, height=40)
label_numbers=ttk.Label(frame_label ,bootstyle='dark', text='result')

frame_label.pack()
label_numbers.pack()

window.mainloop()
