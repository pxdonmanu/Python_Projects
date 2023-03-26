import tkinter as tk
import ttkbootstrap as ttk

# Function that changes the text
def changeText():
  label_one['text']='Text Changed'

def input_text():
  inputTxt=input_cont.get()
  label_two['text']=inputTxt
  input['state']='disabled'

def pick_radio():
  radio_pressed=radio_var.get()
  label_radio['text']=radio_pressed


window=ttk.Window()
window.title('Widgets Tk')
window.geometry('500x650')

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

# Radio Buttons
frameRadio1=ttk.Frame(window)
frameRadio2=ttk.Frame(window)

radio_var=tk.IntVar()
label_radio=ttk.Label(window, textvariable= radio_var)

radio1=ttk.Radiobutton(frameRadio1, text='Radio 1', value=1, variable=radio_var, command=pick_radio)
radio2=ttk.Radiobutton(frameRadio2, text='Radio 2', value=2, variable=radio_var, command=pick_radio)


frameRadio1.pack(pady=15)
radio1.pack()

frameRadio2.pack(pady=5)
radio2.pack()

label_radio.pack(pady=5)

# Text area
frameArea=ttk.Frame(window)

label_textArea=ttk.Label(frameArea, text='Write here!')
text_area=ttk.Text(frameArea, height=10, width=60)

frameArea.pack(pady=15)
label_textArea.pack()
text_area.pack()

# Working with functions that expect a parameter
def button_Func(entry_string):
  print('A button was pressed')
  print(entry_string.get())

  ## If you dont want to use the lambda function
  # def outer_func(parameter):
  #   def inner_func():
  #     print('A button was pressed')
  #     print(parameter.get())
  #   return inner_func
  #
  # and the button would look like this 
  # button_entry=ttk.Button(entryFrame, text='button', command=outer_func(entry_string)) 

entryFrame=ttk.Frame(window)

entry_string=tk.StringVar()
entry=ttk.Entry(entryFrame, textvariable=entry_string)

button_entry=ttk.Button(entryFrame, text='button', command=lambda: button_Func(entry_string)) # The lambda is used to pass the argument to the function

entryFrame.pack(pady=10)
entry.pack(pady=5)
button_entry.pack()

window.mainloop()