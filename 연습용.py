print(" ")
print(" ")


import random as r

# randint, randrange 메서드만 가져오는 방법
# from random import randint, randrange 

# from random import * 
# 이렇게하면 randint 이렇게 변수 형태로 사용가능


lotto = []
for v in range(6):
    x = r.randint(1,45)
    while x in lotto:               # x가 lotto안에 있으면 True니까
        x = r.randint(1,45)    # x를 다시 만들어
    lotto.append(x)

print(f"이번 회차 로또 1등 번호는 {lotto}입니다.")



import random

lotto = []

while len(set(lotto)) != 6:
    lotto.append(random.randint(1,46))

print(f"이번회차 로또 1등 번호는 {set(lotto)}입니다.")








print(" ")
print(" ")