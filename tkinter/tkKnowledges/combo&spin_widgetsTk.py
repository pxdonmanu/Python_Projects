import tkinter as tk
import ttkbootstrap as ttk

window=ttk.Window()
window.title('Combo and spin')
window.geometry('600x400')

label_title=ttk.Label(window, text='Combo ans Spin Buttons', font='Calibri 20 bold')
label_title.pack(pady=25)

# Combo box
items=('Ice Cream', 'Pizza', 'Burger')
food_string=tk.StringVar(value=items[0])
combo_box=ttk.Combobox(window, textvariable=food_string)
# Asign the values to the combo 
combo_box['values']=items

combo_box.pack()

# Events for combo box (What item has been selected)
combo_box.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected value is: {food_string.get()}'))

combo_label=ttk.Label(window, text='Default', font='Calibri 12')
combo_label.pack(pady=10)

# Spin 
spin_int=tk.IntVar(value=0)
spin_box=ttk.Spinbox(window, from_=0, to=100, increment=1, command=lambda: print(spin_int.get()), textvariable=spin_int) # from_=  to=  increment=
spin_box.bind('<<Increment>>', lambda event: print('up'))
spin_box.bind('<<Decrement>>', lambda event: print('down'))

spin_box.pack(pady=10)

# Spin with letters
letters=('A', 'B', 'C', 'D', 'E')
letters_string=tk.StringVar(value=letters[0])
letters_spin=ttk.Spinbox(window, textvariable=letters_string, values=letters)

letters_spin.bind('<<Increment>>', lambda event: print(letters_string.get()))
letters_spin.bind('<<Decrement>>', lambda event: print(letters_string.get()))

letters_spin.pack(pady=10)

window.mainloop()