import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title('Paint mini')
window.geometry('750x770')

# INITIAL STATE OF GLOBAL VARIABLES
brush_color = 'black'
brush_size = 0

# Function to draw
def draw(event):
  x=event.x
  y=event.y
  canvas.create_oval((x-brush_size, y-brush_size, x+brush_size, y+brush_size), fill=brush_color, width=0)

# Function to change brush color
def select_color(event):
  global brush_color
  colors=['red', 'blue', 'yellow', 'green', 'purple', 'pink', 'orange']
  button = event.widget
  # print(f"Button {button.cget('text')} clicked")
  color_map = {
    'RED': colors[0],
    'BLUE': colors[1],
    'YELLOW': colors[2],
    'GREEN': colors[3],
    'PURPLE': colors[4],
    'PINK': colors[5],
    'ORANGE': colors[6]
  }

  button_text = button.cget('text')
  if button_text in color_map:
    brush_color = color_map[button_text]
    return brush_color

# Function to change brush size
def select_size(event):
  global brush_size
  sizes=[1,2,3,4,5]
  size=event.widget

  size_map={
    '1': sizes[0],
    '2': sizes[1],
    '3': sizes[2],
    '4': sizes[3],
    '5': sizes[4]
  }

  button_value=size.cget('text')
  if button_value in size_map:
    brush_size=size_map[button_value]

  return brush_size

# Function to clean the canvas window
def clean(event):
  canvas.delete('all')

# Canvas
frame_canvas=ttk.Frame(window)
canvas=tk.Canvas(frame_canvas, bg='white', width=700, height=450)

### Event to detect when mouse is being clicked
click=canvas.bind("<B1-Motion>", draw)

frame_canvas.pack()

# BUTTONS COLOR
frame_buttonsColor=ttk.Frame(window)

label_color=ttk.Label(frame_buttonsColor, text='BRUSH COLOR', font='Calibri 15 bold')

# Style Buttons
style = ttk.Style()

style.configure("Red.TButton", background="red", foreground="red")
button_color1=ttk.Button(frame_buttonsColor, text='RED', style="Red.TButton")

style.configure("Blue.TButton", background="blue", foreground="blue")
button_color2=ttk.Button(frame_buttonsColor, text='BLUE', style='Blue.TButton')

style.configure("Yellow.TButton", background="yellow", foreground="yellow")
button_color3 = ttk.Button(frame_buttonsColor, text='YELLOW', style='Yellow.TButton')

style.configure("Green.TButton", background="green", foreground="green")
button_color4 = ttk.Button(frame_buttonsColor, text='GREEN', style='Green.TButton')

style.configure("Purple.TButton", background="purple", foreground="purple")
button_color5 = ttk.Button(frame_buttonsColor, text='PURPLE', style='Purple.TButton')

style.configure("Pink.TButton", background="pink", foreground="pink")
button_color6 = ttk.Button(frame_buttonsColor, text='PINK', style='Pink.TButton')

style.configure("Orange.TButton", background="orange", foreground="orange")
button_color7 = ttk.Button(frame_buttonsColor, text='ORANGE', style='Orange.TButton')

# Detect when a button is pressing
button_color1.bind("<Button-1>", select_color)
button_color2.bind("<Button-1>", select_color)
button_color3.bind("<Button-1>", select_color)
button_color4.bind("<Button-1>", select_color)
button_color5.bind("<Button-1>", select_color)
button_color6.bind("<Button-1>", select_color)
button_color7.bind("<Button-1>", select_color)

label_color.pack(pady= 15)
button_color1.pack(side='left', padx=5)
button_color2.pack(side='left', padx=5)
button_color3.pack(side='left', padx=5)
button_color4.pack(side='left', padx=5)
button_color5.pack(side='left', padx=5)
button_color6.pack(side='left', padx=5)
button_color7.pack(side='left', padx=5)

frame_buttonsColor.pack()

# BUTTONS BRUSH SIZE
frame_brushSize=ttk.Frame(window)
label_brush=ttk.Label(frame_brushSize, text='BRUSH SIZE', font='Calibri 15 bold')

button_size1=ttk.Button(frame_brushSize, text='1')
button_size2=ttk.Button(frame_brushSize, text='2')
button_size3=ttk.Button(frame_brushSize, text='3')
button_size4=ttk.Button(frame_brushSize, text='4')
button_size5=ttk.Button(frame_brushSize, text='5')

button_size1.bind("<Button-1>", select_size)
button_size2.bind("<Button-1>", select_size)
button_size3.bind("<Button-1>", select_size)
button_size4.bind("<Button-1>", select_size)
button_size5.bind("<Button-1>", select_size)

label_brush.pack(pady= 15)
button_size1.pack(side='left', padx=5)
button_size2.pack(side='left', padx=5)
button_size3.pack(side='left', padx=5)
button_size4.pack(side='left', padx=5)
button_size5.pack(side='left', padx=5)

frame_brushSize.pack()

# BUTTON CLEAN
frame_clean=ttk.Frame(window)
label_clean=ttk.Label(frame_clean, text='CLEAN WINDOW', font='Calibri 15 bold')
button_clean=ttk.Button(frame_clean, text='Clean')

button_clean.bind('<Button-1>', clean)

frame_clean.pack()
label_clean.pack(pady= 15)
button_clean.pack()

canvas.pack(pady=25)

window.mainloop()