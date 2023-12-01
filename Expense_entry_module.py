'''date format for date entry field. labels getting eaten up upon resize.'''
'''from tkinter import *
from tkinter import messagebox as ms
import csv

def entry():
    data = [e1.get(),e2.get(),e3.get(),e4.get()]
    with open('C:/Users/rithv/WORK/PES/Python/GUI/Expenses.csv','a',newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if data[0] != '' and data[1] != '' and data[2] != '' and data[3] != '':
            csv_writer.writerow(data)
            ms.showinfo('Message','Entry successful')
        else:
            ms.showinfo('Warning!','Please enter a value')

root3 = Tk()
root3.title('Expense entry')
root3.attributes('-fullscreen',True)
amount = Label(root3,text='Expense amount:')
amount.config(font=(24))
amount.place(relx=0.43,rely=0.425,anchor='center')
e1 = Entry(root3,width=20)
e1.place(relx=0.55,rely=0.425,anchor='center')

category = Label(root3,text='Category:')
category.config(font=(24))
category.place(relx=0.457,rely=0.475,anchor='center')
e2 = Entry(root3,width=20)
e2.place(relx=0.55,rely=0.475,anchor='center')

date = Label(root3,text='Date:')
date.config(font=(24))
date.place(relx=0.473,rely=0.525,anchor='center')
e3 = Entry(root3,width=20)
e3.place(relx=0.55,rely=0.525,anchor='center')

description = Label(root3,text='Description:')
description.config(font=30)
description.place(relx=0.45,rely=0.575,anchor='center')
e4 = Entry(root3,width=20)
e4.place(relx=0.55,rely=0.575,anchor='center')

enter = Button(root3,text='Enter',command=entry,width=10,height=2)
enter.place(relx=0.465,rely=0.63,anchor='center')
quit = Button(root3,text='Quit',command=root3.destroy,width=10,height=2)
quit.place(relx=0.535,rely=0.63,anchor='center')

root3.mainloop()'''


from tkinter import *
from tkinter import messagebox as ms
import csv

def entry():
    data = [e1.get(),e2.get(),e3.get(),e4.get()]
    with open("C:/Users/rithv/WORK/PES/Miniproject/Expenses.csv",'a',newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if data[0] != '' and data[1] != '' and data[2] != '' and data[3] != '':
            csv_writer.writerow(data)
            ms.showinfo('Message','Entry successful')
        else:
            ms.showinfo('Warning!','Please enter a value')

root3 = Tk()
root3.title('Expense entry')
root3.attributes('-fullscreen',True)

frame = Frame(root3)
frame.pack(padx=350,pady=300)

amount = Label(frame,text='Expense amount:')
amount.config(font=(24))
amount.grid(row=0,column=0,sticky='e',pady=10)
e1 = Entry(frame,width=20)
e1.grid(row=0,column=1,sticky='w',pady=10)
category = Label(frame,text='Category:')
category.config(font=(24))
category.grid(row=1,column=0,sticky='e',pady=10)
e2 = Entry(frame,width=20)
e2.grid(row=1,column=1,sticky='w',pady=10)
date = Label(frame,text='Date:')
date.config(font=(24))
date.grid(row=2,column=0,sticky='e',pady=10)
e3 = Entry(frame,width=20)
e3.grid(row=2,column=1,sticky='w',pady=10)
description = Label(frame,text='Description:')
description.config(font=24)
description.grid(row=3,column=0,sticky='e',pady=10)
e4 = Entry(frame,width=20)
e4.grid(row=3,column=1,sticky='w',pady=10)

enter = Button(frame,text='Enter',command=entry,width=10,height=2)
enter.grid(row=4,column=0,sticky='e',padx=5,pady=15)
quit = Button(frame,text='Quit',command=root3.destroy,width=10,height=2)
quit.grid(row=4,column=1,sticky='w',padx=5,pady=15)

root3.mainloop()