import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# Canvas
canvas=tk.Canvas(window, bg='#CDB0FF')
canvas.pack()
canvas.create_rectangle((50,30,200,220), fill='#C7F0FF', width=5, dash=(1,2,2,2), outline='red') # create_rectangle((left,top,right,bottom))
canvas.create_line((10,200,200,10), fill='blue', width=5) # create_line((start_x, start_y, end_x, end_y))
canvas.create_oval((240,60,340,160), fill='green', width=2, outline='yellow') # create_rectangle((left,top,right,bottom))
canvas.create_polygon((240,200,260,240,350,200), fill='purple', width=5, outline='#000') # create_polygon((x1,y1, x2,y2, x3,y3, xn,yn))
canvas.create_arc((240,60,340,160), fill='red', width=3, start=45, extent=140, style=tk.PIESLICE, outline='red') # start=angle

canvas.create_text((50,15), text='Text example', fill='red', width=100)

canvas.create_window((120,250), window=ttk.Label(window, text='This is a text in canvas'))

window.mainloop()