print(" ")
print(" ")

# 숫자야구 ~
# 범위는 1 ~ 10 까지, 3개 !
# ex) 3 5 10 했을 때 정답이 10 5 9 라면
# 5는 자리가 맞으니 strike !
# 10은 숫자는 맞지만 자리가 틀리니 ball !
# 3은 아예 없으니까 out !
# 고로 결과는 1 strike, 1 ball, 1 out 이 되겠슴다 ~

import random

# 중복을 어떻게 없애지?ㅋㅋㅋ

chance = 0
strike = 0
ball = 0
out = 0
count = 0
ball1 = 0
ball2 = 0
ball3 = 0


op_gg = 3 # 총 전적
op_gg_win = 3 # 승
op_gg_lose = 0 # 패

# 파일 읽기와 쓰기 왜 안돼이잉
f = open(r'C:\Users\Administrator\Desktop\python\op_gg.txt', '+a')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()



# 난수 생성
baseball_list = []
for i in range(3):
    a = random.randint(1, 10)
    while a in baseball_list:
        a = random.randint(1, 10)
    baseball_list.append(a)

# print(baseball_list)
ready = input("준비되었나?")
op_gg += 1


# 7번만에 맞춰야함
while(ready):
    question1 = int(input("첫번째 자리의 숫자는? :"))
    question2 = int(input("두번째 자리의 숫자는? :"))
    question3 = int(input("세번째 자리의 숫자는? :"))

    for index_list, value in enumerate(baseball_list):
        count += 1
        chance += 1

        # print(f"{index_list+1}자리에 {value}") # 정답 테스트용
        # 스트라이크 계산
        # 자리에 값이 맞아야됨
        if ( question1 == value and index_list+1 == 1 ):
            strike += 1
            question1 = None # ball에서 겹치는거 방지
        elif ( question2 == value and index_list+1 == 2) :
            strike += 1
            question2 = None
        elif ( question3 == value and index_list+1 == 3) :
            strike += 1
            question3 = None

        # 볼 계산 ( 스트라이크가 아닐 때 )
        if(count == 1): 
            ball1 = question1 in baseball_list
            if(ball1):
                ball += 1
        elif(count == 2): 
            ball2 = question2 in baseball_list
            if(ball2):
                ball += 1
        else: 
            ball3 = question3 in baseball_list
            if(ball3):
                ball += 1
        
        

    if(count == 3 and strike != 3):
        if(ball1 == False and question1 is not None):
            out += 1

        if(ball2 == False and question2 is not None):
            out += 1

        if(ball3 == False and question3 is not None):
            out += 1 
        
        print(f"strike : {strike}, ball : {ball}, out : {out}")
        count = 0
        out = 0
        ball = 0
        strike = 0

    if(strike == 3):
        print(f"정답 ~~ {baseball_list}")
        op_gg_win += 1
        break
    
    if(chance == 7):
        print(f"때애에엥 7번의 기회를 모두 썼군요 !\n정답은 {baseball_list}였습니다 ~")
        op_gg_lose += 1
    


print(f"현재 전적\n {op_gg}판 {op_gg_win}승 {op_gg_lose}패")






print(" ")
print(" ")