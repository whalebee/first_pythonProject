import tkinter

def func1(self):
    print("Enter키 입력")

def func2(self):
    print("Entry에서 enter입력")


window = tkinter.Tk()

ent = tkinter.Entry(window,width=20)
ent.pack()

label = tkinter.Label(window, text="click")
label.pack()
label.bind("<Button-1>", func1)


window.mainloop()
    