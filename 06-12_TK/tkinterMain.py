import tkinter

window = tkinter.Tk()

window.geometry("300x200+100+100") # 사이즈 설정 (가로width x 세로height)
window.resizable(True, True) # 사이즈 변경 여부 ( boolean 형으로 ) ( 가로 세로 )

def Button1Click():
    print("버튼 1 클릭")

def Button2Click(num):
    print(f"버튼 {num} 클릭")


btn_1 = tkinter.Button(window, text = "첫번째 버튼", command=Button1Click,
                       width=13, height=4)
# 버튼 만들기, terminal에 print출력됨
# btn_1.pack(side="top")
btn_1.grid(row=0, column=0)

btn_2 = tkinter.Button(window, text = "두번째 버튼", command=lambda:Button2Click(2),
                       width=13, height=4)
# 함수에 매개변수 사용하려면 lambda 써야해
# 안 쓰면 함수를 넘겨주지않고 아예 호출해버려서 한 번밖에 사용이 안 됨
# btn_2.pack(side="bottom")
btn_2.grid(row=1, column=1)





window.mainloop() # 뭐여


