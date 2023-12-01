from tkinter import *
from tkinter import messagebox as ms
import csv

def record():
    data = [entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get()]
    with open("C:/Users/rithv/WORK/PES/Miniproject/Budget_categories.csv",'a',newline='') as csvfile:
        csv_writer=csv.writer(csvfile)
        if data[0] != '' and data[1] != '' and data[2] != '' and data[3] != '':
            csv_writer.writerow(data)
            ms.showinfo('Message:','Data entered successfully')
        else:
            ms.showinfo('Message:','Please enter a value')

root4 = Tk()
root4.title("Centered Labels and Entries")
root4.attributes('-fullscreen',True)
#root4.geometry('1000x500')

frame = Frame(root4)
frame.pack(padx=350, pady=350)  # Adjust padding as needed

labels = ["Budget Name:", "Username:", "Budget Category:", "Budget limit:"]
entries = [Entry(frame) for j in range(len(labels))]

for i, label_text in enumerate(labels):
    label = Label(frame, text=label_text)
    label.config(font=(30))
    label.grid(row=i, column=0, sticky="e")
    entries[i].grid(row=i, column=1,sticky="e")

submit = Button(root4,text='Submit',command=record,width=7,height=2)
submit.place(relx=0.49,rely=0.57,anchor='center')
quit = Button(root4,text='Quit',command=root4.destroy,width=7,height=2)
quit.place(relx=0.535, rely=0.57,anchor='center')

root4.mainloop()

