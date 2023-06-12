import tkinter
import random

# 피드백 : 버튼 2개로 할 것 !


window = tkinter.Tk()


window.geometry("300x200+100+100") # 사이즈 설정 (가로width x 세로height)
window.resizable(True, True) # 사이즈 변경 여부 ( boolean 형으로 ) ( 가로 세로 )


answer = 0 # 다른 함수에서 비교하기위한 전역변수로
v1 = 0
v2 = 0


def Calulate():
    global v1, v2, answer
    my_answer = ent_1.get()
    if str(my_answer) == str(answer):
        # print("Cal의 if부분")
        lbl_a.configure(text="정답입니다!")
        # lbl_q.configure(text=f"{Question()}")
    else:
        # print("Cal의 else부분")
        lbl_a.configure(text=f"오답입니다. \n정답은 : {v1} + {v2} = {answer}였습니다 !")
        # lbl_q.configure(text=f"{Question()}")


def Question():
    # 랜덤 숫자 2개 생성
    first = 1
    last = 100
    global v1, v2, answer
    v1 = random.randint(first, last)
    v2 = random.randint(first, last)
    answer = v1 + v2
    # print(f"answer = {answer}")
    return f"{v1} + {v2} = ?"


# def conf_btn_1():
#     btn_1.configure(text="다른문제")
    
def new_question():
    lbl_q.configure(text=f"{Question()}")


lbl_q = tkinter.Label(window, text=f"{Question()}")
# lbl_q.pack(side='top')
lbl_q.grid(row=0, column=1)

ent_1 = tkinter.Entry(window)
# ent_1.pack(side='top')
ent_1.grid(row=1, column=1)


btn_1 = tkinter.Button(window, text="계산", command=Calulate)
# btn_1.pack(side='top')
btn_1.grid(row=2, column=1)
# btn_1.bind("<Button-1>", lambda click : conf_btn_1())
# lambda를 쓰지 않으면 함수를 넣어주는게 아닌 바로 호출해버림
# -> 함수 안에 print로 확인가능

btn_2 = tkinter.Button(window, text="다른문제", command=new_question)
btn_2.grid(row=3, column=1)

lbl_a = tkinter.Label(window, text="")
# lbl_a.pack(side='top')
lbl_a.grid(row=4, column=1)

# grid 이거 왜 이러는거야ㅋㅋ


window.mainloop()





