#region 
print(" ")
print(" ")

# prompt = """1.Add \n2.Del\n3.List\n4.Quit\nEnter Number : """

# 내가 해서 틀린 거
# num = 0
# while num < 4 :
#     print(prompt, int(input(num)))
#     print(num)
    
# 선생님 버전
# while int(input(prompt)) != 4 :
#     pass # 괄호가 없을 때 그냥 pass 써주면 됨 !


grade = 'F'
score = int(input("성적입력 : "))

# 점수 입력했을 때 들어와서 검사를 해야할 듯?
# 잘 입력했으면 끝나야하고
# 잘못 입력했으면 계속 돌아야하고? -> 애초에 잘입력했어도 while문안에는 들어가야한단말이지?
# 뭔가 지저분한데 ㅋㅋ
# 내가 한 버전
while (score < 0 or score > 100) :
    print("잘못된 입력입니다 다시 입력해주세요")
    score = int(input("성적입력 : "))

if 0 < score < 101 :
    if score >= 90 :
        grade = 'A' 
    elif score >= 80 : 
        grade = 'B' 
    elif score >= 70 : 
        grade = 'C' 
    elif score >= 60 : 
        grade = 'D' 
    elif score < 60  : 
        grade = 'F' 

print("{}점은 {}학점입니다." .format(score, grade))












print(" ")
print(" ")
#endregion


#region while문 예제
print(" ")
print(" ")


# print(type(n)) 

# *
# **
# ***
# ****
# *****
# 5번을 반복해야한다 가정했을 때
# 결국 행과 열을 위해 2번씩 써야함 -> 아니라넹 ~ -> 아니넹 ~

n = int(input("몇 단짜리 별이 보고 싶어요? : "))
i = 0
j = 0

while(i <= n) :
    print("*" * i)
    i += 1
 

print(" ")
print(" ")

# 거꾸로 하려면? 위에서부터 내려오면 됨
i = n
while( i >= 0 ):
    print("*" * i)
    i -= 1


print(" ")
print(" ")
#endregion





#region while문 예제 2번 커피자판기
print(" ")
print(" ")

# 커피 10잔이 한도
# 커피 1잔 = 300원
# 돈을 입력했을 때 그 외의 돈을 다시 돌려줘야한다.
# 남은 커피의 양 출력도 해야하고
# 커피를 모두 팔면 판매중지


# 돈을 넣어주세요

# 거스름돈 있을 때
# 거스름돈 200을 주고 커피를 줍니다 ->  커피 개수 차감
# 커피 잔고 출력


# 다시 돈을 넣어주세요

# 거스름돈 없을 때
# 커피를 줍니다 -> 커피 개수 차감
# 커피 잔고 출력


# 다시 돈을 넣어주세요
# 돈이 모자를 때
# 돈을 다시 돌려주고 커피를 주지 않는다 -> 개수 일정
# 커피 잔고 출력

# 커피 원해?

coffee = 10

# 커피가 1잔 이상 있을 때 계속 판매
while(coffee > 0) :
    money = int(input("돈을 넣어 주세요 : "))

    if (money < 300) :
        print("돈이 부족합니다.")
    elif (money == 300) :
        print("커피 한 잔을 드립니다.")
        coffee -= 1
    else :
        # 3000원을 주든 30000원을 주든 한 잔만 파는 중 ( 자판기라서 )
        change =  money - 300
        print(f"거스름돈 {change}원을 드리고 커피를 한 잔 드립니다.")
        coffee -= 1
        
    print(f"남은 커피의 수량은 {coffee}잔 입니다.")

print("커피가 모두 판매되었습니다. \n판매를 종료합니다 ^ㅡ^")


print(" ")
print(" ")
#endregion





#region 반복문-1)
print(" ")
print(" ")

# print(list(range(1,6)))

for value in range(1,6):
    print(value, end=" ")
# 1 2 3 4 5
print("")
for value in range(5,0,-1):
    print(value, end=" ")
# 5 4 3 2 1

total = 0
score_list = [95,100,80,90,77]

for score in enumerate(score_list):
    print(score)
# 인덱스 자리도 같이 나옴

for i, score in enumerate(score_list):
    print(f"{i+1}번째 점수는 {score} 입니다.")
    total += score

print(f"총점은 {total} 입니다.")


grade = {"이름":"danaka", "학년":"3", "성적":"A"}
# print(grade.keys())
# print(grade.values())
# print(grade.items())

# for item in grade:
#     print(item)
# # 이름 학년 성적


# 같은 것임 ( 표현만 다를 뿐 )
for key, value in grade.items():
    print("key: "+ key, "value: "+value)

# for key, value in grade.items():
#     print("key:", key, "value:",value)

print(" ")
print(" ")
#endregion







#region 반복문 2)
print(" ")
print(" ")

meter_list = [1,3,5,7]
cm_list = [100 * i for i in meter_list]
print(cm_list)
# [100, 300, 500, 700]

list_a = [1,2,3,4,5]
result = []
for x in list_a:
    result.append(x*x)
print(f"리스트 함수 사용 : {result}")
# 리스트 함수 사용 : [1, 4, 9, 16, 25]

result = [i * i for i in list_a]
print(f"반복문 사용해서 한 번에 : {result}")
# 반복문 사용해서 한 번에 : [1, 4, 9, 16, 25]


list_a = [1,2,3,4,5]
result = [x*x for x in list_a if(x%2 == 0)]
print(result)
# [4, 16]


# 구구단
result = [x*y for x in range(2,10) for y in range(1,10)]
print(f"전체 다\n{result}")

print("")

result2 = [x*y for x in range(2, 10) if ( x%2 == 0 ) for y in range (1, 10)]
print(f"짝수만\n{result2}")


print(" ")
print(" ")
#endregion








#region 리스트와 반복문을 이용한 예제 1 ~ 6번 ( 난수 맞추기 문제 )
print(" ")
print(" ")

# ex1
for i in range(2,10) :
    print(f"----{i}단----")
    for j in range(1,10) :
        print(f"{i} x {j} = {i*j}")

# ex2
num = []
plus = []
minus = []

for i in range(10):
    put_num = int(input("정수를 입력하세요 :"))
    num.append(put_num)

for x in num :
    if (x > 0) :
        plus.append(x)
    else:
        minus.append(x)

print(f"입력받은 정수는 : {num}입니다.")
print(f"그 중 양수는 {plus} 이며, 음수는 {minus} 입니다 .")

# ex3
total = 0
avg = 0

grade_list = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i, grade in enumerate(grade_list) :
    total += grade
avg = total / i
print(f"총점은 : {total}")
print(f"평균은 : {avg}")
    



# ex4
result = [x for x in grade_list if( x < avg ) ]
print(f"평균미만의 값들은 : {result}")




# ex5

import random		
# ex5 = random.randint(a, b)	# a ~ b 범위에 있는 정수를 난수로 반환
# print(ex5)

# 먼저 컴퓨터가 난수를 생성하고 맞출 때까지 못나가 !
# 랜덤 수 샌성
a = 1
b = 1000
import random       # 내장 함수 아니기에 import 필요
c_random = random.randint(a, b)
# print(c_random) # 테스트용

# while(c_random) :
#     correct = int(input("컴퓨터가 만든 숫자는?"))
#     if(c_random == correct):
#         print("정답입니다 ㅎㅎ 종료할게요")
#         break
#     else :
#         print("땡 !!!")
    
while(c_random) :
    correct = int(input("컴퓨터가 만든 숫자는?"))
    if(c_random > correct):
        print("땡 !! UP !")
        continue
    elif( c_random < correct):
        print("땡 !! Down !")
        continue
    else :
        print("정답입니다 ㅎㅎ 종료 !")
        break


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
goal = start + 25
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
#endregion








#region 



#endregion





