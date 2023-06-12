import tkinter

window = tkinter.Tk()

window.geometry("300x200+100+100") # 사이즈 설정 (가로width x 세로height)
window.resizable(True, True) # 사이즈 변경 여부 ( boolean 형으로 ) ( 가로 세로 )

def Button1Click():
    print(f"버튼 1 클릭")

def Button2Click():
    print(f"버튼 2 클릭")


btn_1 = tkinter.Button(window, text = "첫번째 버튼", command=Button1Click)
# 버튼 만들기, terminal에 print출력됨
btn_1.pack()

btn_2 = tkinter.Button(window, text = "두번째 버튼", command=Button2Click)
btn_2.pack()





window.mainloop() # 뭐여


