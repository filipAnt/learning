'''
First short project to create simple calculator with GUI
'''

import tkinter as tk
from tkinter import *

main_window = Tk()
main_window.title('Calculator')
main_window.geometry('500x300')
main_entry = Entry(main_window, bd=5, width=500)
main_entry.pack()

class Operations():
    def option(self):
        options = ['plus', 'minus', 'multiply', 'divide']


plus_button = tk.Button(main_window, text='+', justify='center')
plus_button.pack()




main_window.mainloop()