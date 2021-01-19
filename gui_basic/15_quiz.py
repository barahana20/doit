"""
    1. title : 제목 없음 - Windows 메모장
    2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
    3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
    3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
    3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
    3-3 끝내기 : 프로그램 종료
    4. 프로그램 시작 시 본문은 비어 있는 상태
    5. 하단 status 바는 필요 없음
    6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
    7. 본문 우측에 상하 스크롤 바 넣기
"""
import sys
import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
# root.geometry("640x480") # 가로 x 세로 지정
root.geometry("640x480") # 가로 x 세로 + x좌표 + y좌표

filename = "mynote.txt"

root.resizable(True, True) # x(너비), y(너비) 값 변경 불가 ( 창 크기 변경 불가 )

def open_file():
    f = open_file("mynote.txt", 'r')
    text.delete("1.0",END)
    text.insert(END, f.read())
def save_file():
    f = open_file("mynote.txt", 'w')
    f.write(text.get("1.0",END))

menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="종료",command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집
menu.add_cascade(label="편집")
# 서식
menu.add_cascade(label="서식")
# 보기
menu.add_cascade(label="보기")
# 도움말
menu.add_cascade(label="도움말")

# label = Label(root, text="메모장")
# label.pack()


# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill='y')

# text 지정
text = Text(root, yscrollcommand=scrollbar.set) # 크기 지정하는거 유튜브 잘 보기
text.pack(side="left",fill="both", expand=True)


text.config(yscrollcommand=scrollbar.set)


root.config(menu=menu)


root.mainloop()