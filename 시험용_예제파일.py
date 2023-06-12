#region 조건문 if의 예제 1, 2번 ( 교통카드, 환전 )
print(" ")
print(" ")

# ex1
age = input("나이를 입력해주세요 (만 나이, 7 이상 입력) :")
age = int(age)
# print(type(age))
money = 10000
# print(type(money))
print(f"현재 교통카드의 잔액은 {money}입니다.")

# 그러네 큰 것부터 시작하는게 더 낫겠네
if(age >= 19) :
    money -= 1250
elif(age >= 13) :
    money -= 1050
elif (age >= 7) :
    money -= 650
elif(age < 7):
    print("6세 이하는 무료입니다.")
else :
    print("잘못입력했습니다")
    exit()
    
print(f"남은 잔액 : {money}")



fund_money = int(input("가지고 싶은 돈은 얼마 인가요? ( 10만원 이상 ) : "))
# fund_money = int(fund_money) 이렇게 하는 건 별로니까네 ~
if(fund_money < 100000):  # 235800 이면? 4매, 3매, 1매, 1개, 3개
    print("기초 자금이 부족합니다. ")
    exit()
else:
    money_1 = fund_money // 50000
    fund_money = fund_money % 50000
    print(f"5만원권으로는 {money_1}매 나옵니다.")

    money_2 = fund_money // 10000
    fund_money = fund_money % 10000
    print(f"만원권으로는 {money_2}매 나옵니다.")

    money_3 = fund_money // 5000
    fund_money = fund_money % 5000
    print(f"오천원권으로는 {money_3}매 나옵니다.")

    money_4 = fund_money // 1000
    fund_money = fund_money % 1000
    print(f"천원권으로는 {money_4}매 나옵니다.")

    money_5 = fund_money // 500
    fund_money = fund_money % 500
    print(f"오백원으로는 {money_5}개 나옵니다.")

    money_6 = fund_money // 100
    fund_money = fund_money % 100
    print(f"백원권으로는 {money_6}개 나옵니다.")


# ex2 아이 잘못했넹
# fund_money = input("가지고 싶은 돈은 얼마 인가요? ( 10만원 이상 ) : ")
# fund_money = int(fund_money)
# if(fund_money < 100000):
#     print("기초 자금이 부족합니다. ")
#     exit()
# else:
#     choice = input("5만원권:1 , 만원권:2, 오천원권:3, 천원권:4, 오백원:5, 백원:6 이 중에서 고르세용 : ")
#     choice = int(choice)
#     if choice == 1:
#         money_1 = fund_money/50000
#         print(f"5만원권으로는 {int(money_1)}매 나옵니다.")
#     elif choice == 2:
#         money_2 = fund_money/10000
#         print(f"만원권으로는 {int(money_2)}매 나옵니다.")
#     elif choice == 3:
#         money_3 = fund_money/5000
#         print(f"5천원권으로는 {int(money_3)}매 나옵니다.")
#     elif choice == 4:
#         money_4 = fund_money/1000
#         print(f"천원권으로는 {int(money_4)}매 나옵니다.")
#     elif choice == 5:
#         money_5 = fund_money/500
#         print(f"500원으로는 {int(money_5)}개 나옵니다.")
#     elif choice == 6:
#         money_6 = fund_money/100
#         print(f"100원으로는 {int(money_6)}개 나옵니다.")
#     else :
#         print("지정된 숫자 이외의 다른 문자가 입력되었으니 종료합니다. 왜냐하면 반복문을 모르거든요")
#         exit()



print(" ")
print(" ")
#endregion




#region 문제
print(" ")
print(" ")

# ex4
list_a = [1,3,5,4,2]
list_a.sort(reverse=True)
print(f"4번 : {list_a}")


# ex5
str_a = ['Life', 'is', 'too', 'short']
result = ' '.join(str_a)
print(f"5번 : {result}")
# Life is too short


# ex6 
tuple_a = (1,2,3)
tuple_a = tuple_a + (4,)
print(f"6번 : {tuple_a}")
# (1, 2, 3, 4)


# ex7 
dic_a = {'A':90, 'B':80, 'C':70}
print(f"7-1번 : {dic_a['B']}")
# 80
del dic_a['B']
print(f"7-2번 : {dic_a}")
# {'A': 90, 'C': 70}

dic_a = {'A':90, 'B':80, 'C':70}    # 이거 다시 추가해줌
print(f"7-3번 : {dic_a.pop('B')}")  # 이거 왜 안되징 -> B가 이미 삭제되었었으니까
print(f"7-4번 : {dic_a}")


# ex8
list_a = [1,1,1,2,2,3,3,3,4,4,5]
list_b = list(set(list_a)) # 집합으로 나온 dict -> list로 변경 !
print(f"8번 : {list_b}")
# [1, 2, 3, 4, 5]


# ex9
list_a = list_b = [1,2,3]
list_a[1] =4
print(f"9번 : {list_b}")
# [1, 4, 3]
# list_a와 list_b는 같은 주소를 바라보고 있기 때문에
# list_a의 인덱스 1의 자리의 값을 바꿔주었을 때
# list_b를 출력해도 바꿔준 값을 출력해준다.
# 확인 방법
print(f"9번 검증 list_a의 id : {id(list_a)}")
print(f"9번 검증 list_b의 id : {id(list_b)}")




print(" ")
print(" ")
#endregion





# 중복 없애는 방법
baseball_list = []
for i in range(3):
    a = random.randint(1, 10)
    while a in baseball_list:
        a = random.randint(1, 10)
    baseball_list.append(a)




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
avg = total / (i+1)
# print(i+1) -> 인덱스가 10개지만 마지막 인덱스의 자리가 9라서 !!
# 아니면 걍 len 써
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
    time_exceed = now - goal
    if(now > goal) :
        print("시간초과 ㅎㅎ")
        print(f"경과된 시간은 : {int(time_exceed)}초네요ㅎㅎ")
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









b_days = input("생일을 입력하세요 (형식 : mm/dd) :").split(' ')

# print(b_days)

la_date = lambda x : f"{x.split('/')[0]:0>2}월{x.split('/')[1]:0>2}일"
result = ' '.join(map(la_date, b_days))

print(result)





def factorial(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 1: # else 아님 주의 !! else면 무조건 1만 나오잖어ㅋㅋ
        return 1
    return n * factorial(n-1)














#region 함수 정의 예제
print(" ")
print(" ")

# ex1
# 함수 정의
def ex1(*args) :
    result = 0
    for value in args:
        result += value

    return result

# 매개변수 설정
ex1_sum = ex1(3, 5, 8)

# 결과 확인
print(f"1번문제 : {ex1_sum}")




# ex2 -> 내장함수 사용하여 최대값, 최소값 구하기
list_ex2 = [52,273,103,32,57]
# print(min.__doc__)
print(f"2번문제 최소값 : {min(list_ex2)}")
print(f"2번문제 최대값 : {max(list_ex2)}")




# ex3
def custom_min(*args):
    min = args[0]
    for x in args:
        if x < min:
            min = x
    return min

list_3_min = custom_min(10, 30, 40 ,50 ,60 ,70, 3, -5)
print(f"3번문제 커스텀 최소값 : {list_3_min}")

def custom_max(*args):
    max = 0
    for x in args:
        if x > max:
            max = x
    return max
list_3_max = custom_max(10, 30, 40, 50, 60, 70)
print(f"3번문제 커스텀 최대값 : {list_3_max}")



# ex4
def divide(x, y):
    quotient = x // y
    remainder = x % y
    # print(f"{x} // {y} = {x // y} (몫)") # 몫
    # print(f"{x} % {y} = {x % y} (나머지)") # 나머지
    return quotient, remainder
# print(f"4번문제 : {divide(10, 6)}")
v1, v2 = divide(10, 6)
print(f"4번문제 몫은 : {v1}")
print(f"4번문제 나머지는 : {v2}")




# ex5
# 재귀함수 아닌 버전
# def palindrome(str_a):
#     str_a = str_a.replace(" ", "") # 공백 제거 ( 띄어쓰기 때문에 )
#     count = 0
#     p = 0
#     m = -1
#     for v in str_a:
#         if str_a[p] == str_a[m]:
#             count += 1
#         # print(str_a[p])
#         # print(str_a[m])
#         p += 1
#         m -= 1
#     if ( count == len(str_a)):
#         return True
#     else:
#         return False
        
# 재귀함수 버전 -> 맞는데 최적화 필요
# def palindrome(str_a):
#     str_a = str_a.replace(" ","") 

#     def palindrome_re(str_a, first, last):
#         if first >= last:
#             return True
#         elif str_a[first] != str_a[last]:
#             return False
#         else:
#             return palindrome_re(str_a, first + 1, last - 1)

#     return palindrome_re(str_a, 0, len(str_a) - 1) # 인덱스의 범위때문에 -1 해줘야됨
        

def palindrome(str_a):
    # str_a = str_a.replace(" ","")
    print(str_a[1:-1])
    if len(str_a) <= 1:
        return True
    if str_a[0] != str_a[-1]:
        return False
    
    return palindrome(str_a[1:-1])


# 다른 방법예제 ( 재귀함수 X )
# def is_palindrome(string):
#     if string == string[::-1]:
#         return True
#     else:
#         return False


print(palindrome("역삼역")) # True
print(palindrome("12345678987654321")) # True
print(palindrome("123454231")) # False
print(palindrome("repaper")) # True
print(palindrome("다리 그리고 저고리 그리다")) # True
print(palindrome("다리 그리고 저고라 그리다")) # False
print(palindrome("1 2 321")) # True
print(palindrome("was it a cat i saw")) # True
#endregion