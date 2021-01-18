from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # 1.0에서 1은 라인 1부터 가져와라 0은 칼럼기준으로 0부터 가져와라 라는 뜻
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0,END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()




root.mainloop()

