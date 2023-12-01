'''from tkinter import *

root = Tk()
root.title("Using Frames")
#root.attributes('-fullscreen',True)
root.geometry('1000x700')

frame = Frame(root)
frame.pack(padx=300,pady=350)

lb1 = Label(frame,text='Label 1:')
lb1.grid(row=0,column=0,sticky='w',pady=15)
lb2 = Label(frame,text='Label 2:')
lb2.grid(row=1,column=0,sticky='w',pady=15)
exit = Button(frame,text='Exit',command=root.destroy,width=5,height=2)
exit.grid(row=2,column=0,sticky='w',pady=15)

pic = Canvas(root,width=root.winfo_screenwidth(), height=root.winfo_screenheight())
filename = PhotoImage(file="C:/Users/rithv/WORK/PES/Python/GUI/demo.png")
pic.create_image(0,0,anchor='nw',image=filename)
pic.pack(fill=BOTH,expand=True)

root.mainloop()'''

from tkinter import *


main_root = Tk()
main_root.title('Budget tracker')
main_root.attributes('-fullscreen',True)

# Load the image using Tkinter's PhotoImage
image_path = 'C:/Users/rithv/WORK/PES/Miniproject/coins.png'  # Replace with the actual path to your image file
img = PhotoImage(file=image_path)

# Create a label with the image
background_label = Label(main_root, image=img)
background_label.place(relwidth=1, relheight=1)

frame = Frame(main_root)
frame.pack(padx=300,pady=350)

# Add your main module content on top of the image label...
# For example:
label = Label(frame, text="Main Module Content", font=('Helvetica', 24, 'bold'))
label.grid(row=0,column=0,sticky='w',pady=0)
quit = Button(frame, text='Quit', command=main_root.destroy)
quit.grid(row=1,column=0,sticky='w',pady=10)

main_root.mainloop()

