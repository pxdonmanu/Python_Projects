import tkinter as tk

window=tk.Tk()
window.title('Paint mini')
window.geometry('500x400')

# Function to draw
# def detect_click(click_string):
#   click=click_string.get()
#   if click==1:
#     print('Cliked')
#   else:
#     print('Uncliked')

brush_size=2
# Canvas
canvas=tk.Canvas(window, bg='white', width=450, height=350)
# detects cursor movement in the frame

###### cursor=canvas.bind('<Motion>', lambda event: print())

# detects when a click is made inside the frame
click_string=tk.IntVar(value=1)

###### click=canvas.bind('<ButtonRelease-1>', lambda event: detect_click(click_string))

canvas.pack(pady=25)

window.mainloop()