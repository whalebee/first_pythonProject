import tkinter

window = tkinter.Tk()


def Calulate():
    lbl_1.configure(text="결과 값 :"+ str(eval(ent_1.get())))
# ent_1의 텍스트 내용을 가져와 -> get함수
# eval "1+1" 이런 것들을 실제로 계산해줌


ent_1 = tkinter.Entry(window) # 한 줄 텍스트 위젯
ent_1.grid(row=0, column=0)

btn_1 = tkinter.Button(window, text="계산", command=Calulate)
btn_1.grid(row=0, column=1)

lbl_1 = tkinter.Label(window) # 텍스트, 이미지 위젯
lbl_1.grid(row=0, column=2)

window.mainloop()