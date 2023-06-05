print(" ")
print(" ")

# ex6
a = 1
b = 100
import random
first = 1
last = 100
count = 0
question = 0
answer = 0

ready = input("준비되었나요! : ")
# 시작하면 카운트 시작 !
import time
start = time.time()
goal = start + 5
# print(start)
# print(goal)

while(ready):
    # print(count) 테스트용
    first = random.randint(a, b)
    last = random.randint(a, b)
    answer = first+last
    question = int(input(f"{first} + {last} = "))
    now = time.time()
    dif_time = goal - now
    if(now > goal) :
        print("시간초과 ㅎㅎ")
        print(f"경과된 시간은 : {int(dif_time)}초네요ㅎㅎ")
        break
    else :
        if( answer != question) :
            print(f"땡 !!! 정답은 {answer} 이였습니다ㅎㅎ ")
            break
        elif ( answer == question):
            print("Bingo !!")
            count += 1
            if (count == 5) :
                print("Complete !")
                print(f"걸린 시간 : {int(dif_time)}초")
                break

print("end of program")











print(" ")
print(" ")