# -*- coding: utf-8 -*- 
from tkinter import *

def btn1_command():
    print("dd")


def inventory():
   root = Tk()
   root.title("INVENTORY")
   # root.geometry("640x480") # 가로 x 세로 지정
   root.geometry("320x480") # 가로 x 세로 + x좌표 + y좌표
   root.resizable(True, False) # x(너비), y(너비) 값 변경 불가 ( 창 크기 변경 불가 )

   label1 = Label(root, text="안녕하세요")
   label1.pack(side='left')


   btn1 = Button(root, padx=10, pady=5, text="버튼3", command=btn1_command) # 버튼 크기 유동성
   btn1.pack(side='right')


   root.mainloop()

inventory()