import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# Function convert
def convert():
  kilometer_input=entry_int.get()
  miles=kilometer_input*0.62137
  output_string.set(miles)

# Window

window=tk.Tk()
# window title
window.title('Converter')
# size of the window
window.geometry('350x200') # geometry(widthxheight)

# Title (inside the window)
title_label=ttk.Label(master=window, text='Kilometers to miles', font='Calibri 18 bold') # font='font fontsize '
# put the label on a "div" inside the window
title_label.pack(pady=22)

# Input field
input_frame=ttk.Frame(master=window)
# Anything that will be put into the input will be stored in the entryInt variable
entry_int=tk.IntVar()
entry=ttk.Entry(master=input_frame, textvariable=entry_int)
button=ttk.Button(master=input_frame, text='Convert', command=convert) # command is like an onPress
# entry and button are inside the input_frame and the input_frame is inside the window
# the .pack() method is used to put the widgets inside the window
input_frame.pack(pady=5) # pady is padding in y and its value is 20px
entry.pack(side='left', padx=10) # padx is padding in x and its value is 10px
button.pack(side='left')

# Output
output_string=tk.StringVar()
output_label=ttk.Label(master=window, text='Output', font='Calibri 15', textvariable=output_string)
output_label.pack(pady=20)


# Run
window.mainloop() # The windows appears