import tkinter as tk
from tkinter import ttk

# Function for the operations
def add():
  num1=input1_float.get()
  num2=input2_float.get()

  add_num=num1+num2

  output_string.set(add_num)

def sub():
  num1=input1_float.get()
  num2=input2_float.get()

  sub_num=num1-num2

  output_string.set(sub_num)

def mult():
  num1=input1_float.get()
  num2=input2_float.get()

  sub_num=num1*num2

  output_string.set(sub_num)

def div():
  num1=input1_float.get()
  num2=input2_float.get()

  sub_num=num1/num2

  output_string.set(sub_num)

# Window 
window=tk.Tk()
window.title('Basic Calculator')
window.geometry('350x250')

# Main Text
text_label=ttk.Label(master=window, text='Calculator', font='Calibri 20 bold')
text_label.pack(pady=20)

# Inputs
input_frame=ttk.Frame(master=window)

input1_float=tk.DoubleVar()
input_one=ttk.Entry(master=input_frame, textvariable=input1_float)

input2_float=tk.DoubleVar()
input_two=ttk.Entry(master=input_frame, textvariable=input2_float)

input_frame.pack()
input_one.pack(side='left', padx=10)
input_two.pack(side='left')

# Buttons
buttons_frame=ttk.Frame(master=window)
btn_add=ttk.Button(master=buttons_frame, text='+', command=add)
btn_subtract=ttk.Button(master=buttons_frame, text='-', command=sub)
btn_multiply=ttk.Button(master=buttons_frame, text='*', command=mult)
btn_divide=ttk.Button(master=buttons_frame, text='/', command=div)

buttons_frame.pack(pady=30)
btn_add.pack(side='left')
btn_subtract.pack(side='left')
btn_multiply.pack(side='left')
btn_divide.pack(side='left')

# Output
output_string=tk.StringVar()
output_label=ttk.Label(master=window, textvariable=output_string , font='Calibri 16')
output_label.pack()


# MUST ALWAYS COME AT THE END
window.mainloop()
