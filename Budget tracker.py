from tkinter import *
from tkinter import messagebox as ms
from Authentication_module import verification, click
import csv

def auth():
    import Authentication_module

def opt1():
    import Expense_entry_module

def opt2():
    import Budget_category_module

def opt3():
    import Budget_history_module

def main_mod():
    root = Tk()
    root.title('Budget tracker')
    root.attributes('-fullscreen',True)
    menu_font = (24)
    menu_bar = Menu(root,font=24)
    root.config(menu = menu_bar)
    file_menu = Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label='Menu', menu=file_menu)
    file_menu.add_command(label='opt 1',command=opt1)
    file_menu.add_command(label='opt 2',command=opt2)
    file_menu.add_command(label='opt 3',command=opt3)
    file_menu.add_command(label='Quit',command=root.destroy)
    root.mainloop()

def main_func():
    verification()
    if verification():
        main_mod()
main_func()
