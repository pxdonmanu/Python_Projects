import tkinter as tk
import ttkbootstrap as ttk

window=ttk.Window()
window.title('Events')
window.geometry('600x500')

# Functions
def get_pos(event):
  print(f'x: {event.x} y: {event.y}')

# Widgets
text=ttk.Text(window)
text.pack()

entry=ttk.Entry(window)
entry.pack(pady=10)

btn=ttk.Button(window, text='A button')
btn.pack(pady=5)

# Events
## If alt+a is pressed while the program is running, 'an event' will appear in the console.
btn.bind('<Alt-KeyPress-a>', lambda event: print('an event')) # bind(event, function) ('modifier-type-detail', function)

### In this website there are more events https://www.pythontutorial.net/tkinter/tkinter-event-binding/

# EVENT TO GET THE MOUSE POSITION
window.bind('<Motion>', get_pos)

# EVENT TO DETECT EACH KEY PRESS
window.bind('<KeyPress>', lambda event: print(f'a key was pressed ({event.char})'))    

# EVENT TO DETECT IS THE ENTRY FIELD WAS BEING SELECTED
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# EVENT THAT PRINT 'MouseWheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

window.mainloop()