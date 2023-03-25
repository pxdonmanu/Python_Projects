import tkinter as tk
import ttkbootstrap as ttk

# Function that changes the text
def changeText():
  label_one['text']='Text Changed'

def input_text():
  inputTxt=input_cont.get()
  label_two['text']=inputTxt
  input['state']='disabled'

window=ttk.Window()
window.title('Widgets Tk')
window.geometry('500x280')

# Checkbutton
frameCheck=ttk.Frame(window)
check_var=tk.IntVar()
check_button=ttk.Checkbutton(frameCheck, 
                            text='Check', 
                            command=lambda:print(check_var.get()), # Print 1 or 0 (check or uncheck)
                            variable=check_var)
label_check=ttk.Label(frameCheck, textvariable=check_var)

frameCheck.pack(pady=20)
check_button.pack(side='left', padx=5)
label_check.pack(side='left')

# Button that changes a text
label_one=ttk.Label(window, text='Text')
button=ttk.Button(window, text='Change the title', command=changeText)

label_one.pack(pady=5)
button.pack(pady=5)

# Button that changes the label text with the input text
label_two=ttk.Label(window, text='You can write')
input_cont=tk.StringVar()
input=ttk.Entry(window, textvariable=input_cont)
button2=ttk.Button(window, text='Click!', command=input_text)

label_two.pack(pady=5)
input.pack(pady=5)
button2.pack(pady=5)


window.mainloop()