from tkinter import *

root = Tk()
root.title("Nado Coding")
root.geometry("640x480")


label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="./gui_basic/img.png")
label2 = Label(root, image=photo)


root.mainloop()