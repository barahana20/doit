from tkinter import *
import nourish_sword as n_s

def aa():
   root = Tk()
   root.title("INVENTORY")
   # root.geometry("640x480") # 가로 x 세로 지정
   root.geometry("320x480") # 가로 x 세로 + x좌표 + y좌표

   root.resizable(True, False) # x(너비), y(너비) 값 변경 불가 ( 창 크기 변경 불가 )

   print(n_s.screen_height)


   root.mainloop()

