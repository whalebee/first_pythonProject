print(" ")
print(" ")


# call_cal.py

import calculator
# print(calculator.add(10, 20)) # 가능

# from calculator import add
# print(add(10, 20))

calc_a = calculator.Calc(30, 2)
calc_b = calculator.Calc(50, 20)

print(calc_a.add())
print(calc_b.add())



# import desktop # 지금은 불가능

import sys
print(sys.path) # 이 안에 있는 디렉토리만 사용이 가능

# 왜 3가지 방법이 다 되는걸까나 .. 흠흠
# sys.path.append("C:\\Users\\Administrator\\Desktop\\python\\first\\first_pythonProject")
sys.path.append(r"C:/Users/Administrator/Desktop/python/first/first_pythonProject/")
# sys.path.append(r"C:\Users\Administrator\Desktop\python\first\first_pythonProject")
print(sys.path)

print(" ")
print(" ")

import 임시용_update_06_09.desktop_for_sys as desktop_for_sys
desktop_for_sys.desktop() # 왜 안되지ㅋㅋ # ? 지금은 왜 또 되지ㅋㅋ

print(" ")
print(" ")