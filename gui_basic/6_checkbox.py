from tkinter import *
import pygame

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100")

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()
# chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()




root.mainloop()

