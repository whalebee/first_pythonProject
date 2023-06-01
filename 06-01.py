# ----------------------------------------------
# -----------------------------------------------------------------------------------------------
print(" ")
print(" ")


#region 인덱스 응용-1 & 문제
print(" ")
print(" ")
# 인덱스 응용
nested_list2=["Hello!", [1,2,3], ["Hi Python", 4, [5,6,7]]]

# 출력해야할 것들
# Hello! Hi Python
# 4,5

a = nested_list2[2][1]
b = nested_list2[2][2][0]

print(nested_list2[0], nested_list2[2][0])
print(f"{a},{b}")


# ----------------------------------------------
# 출력해야할 것들
# 5,6
# Python

print(nested_list2[2][2][:2])
print(nested_list2[2][0][3:])

print(" ")
print(" ")
#endregion







#region 리스트 기본 & 문제
print(" ")
print(" ")
list1 = [1, 2, 3]
# str(list1) + "Hi"   # 가능
# list1 + "Hi"      # 불가능
print(list1*3) # 123 123 123 이렇게 3개


list1 = [1,2,3]
list2 = list1 + list("Hi")
list3 = str(list1) + "Hi"
print(list2)
print(list3)


my_list=[]
# 추가
my_list.append(1) 
print(my_list)
my_list.append(2)
# [1, 2]

# 삽입
my_list.insert(1,3) 
# [1, 3, 2] -> 1자리에 3이 넣어지고 그 뒤는 밀려남

# 확장
my_list.extend([4,5,6])
# [1,3,2,4,5,6]

# 추가로 리스트를 넣으면 [] 가 더 들어가짐 (중복)
my_list.append([7,8])
# [1,3,2,4,5,6, [7,8]]

# 단순 연산 ( 대입이 아님 )
my_list2 = [9,10]
# print(my_list+my_list2)

# pop은 인덱스를 다룸
my_list.pop()
# [7, 8]
# 그 다음 print my_list 해보면 [7,8]이 사라짐
my_list.pop(1) # 이러면 인덱스 1의 자리에 있는 3이 사라짐

my_list.remove(1) # 인덱스가 아니라 value를 다룸
# print(my_list) 0의 자리에 있는 1 value가 사라짐

# 리스트 안의 값들이 사라짐
my_list.clear()
del my_list[:]

# 리스트 자체가 사라짐
del my_list

# 특정범위만 지우기도 가능
# del my_list[:2]
# my_list[0:2] = []
# 같은 뜻

# 실습
my_list=[1,2,3,'a','b','c']
# pop, remove, del, [] 각각 사용해서 지워보기

# index를 기준으로 하는 pop
print(my_list.pop())
print(my_list)
# [1, 2, 3, 'a', 'b']

# remove는 value를 지우는거라 문자 지우고 싶으면 문자형식을 써줘야함
print(my_list.remove('a')) 
print(my_list)
# [1, 2, 3, 'b']

del my_list[:1]
print(my_list)
# [2, 3, 'b']

my_list[:3] = []
print(my_list)
# []

# 정렬
my_list=[4,3,1,2,5]
print(my_list.sort()) # [1,2,3,4,5]
print(my_list.reverse()) # [5,4,3,2,1]
print(my_list.sort(reverse=True)) # sort와 reverse를 한 번에 [5,4,3,2,1]


# count 
my_list3=['a','b','d','d']
print(my_list3.count('d')) # 2 개수

print(my_list3.index('d')) # 2 d가 있는 자리


list1=[1,2,3]
list2=list1
list2[0] = 4
print(list1, list2) # 주소를 참조해서 바꾸는 것 => 얕은 복사
# [4,2,3] [4,2,3]

# 둘 다 id가 같음 ! ( 같은 곳을 바라보기 때문 )
print(id(list1)) 
print(id(list2))

list2 = list1.copy()
list2[0] = 1
print(list1, list2)
# [4,2,3] [1,2,3]
# 서로 id도 다름

# print(list2 = list1[:]) # 뭐지 오류남 ㅋㅋ
# print(list2 = list(list1))
# print([] + list1)


# ?? 잤다 
# tuple은 () 이런 형식으로 쓰이는 것 같음
list1=[1,2,3,[4,5]]
import copy
list2=copy.deepcopy(list1)

fruit = ['strawberry','peach', 'banana', 'melon', 'orange']
print(fruit[2:4], fruit[::2])
# ['banana', 'melon'] ['strawberry', 'banana', 'orange']

print(" ")
print(" ")
#endregion






#region 딕셔너리
print(" ")
print(" ")

# 딕셔너리
user={'name':'홍길동', 'age':20}
print(user.keys())      # dict_keys(['name', 'age'])
print(user.values())    # dict_values(['홍길동', 20])
print(user.items())     # dict_items([('name', '홍길동'), ('age', 20)])


# 반복문 데모
for key, value in user.items():
    print("key는 : %s" %key)
    print("value는 : %s " %value)

print('name' in user) # True
print('phone' in user) # False

# key = value 형식으로 user 딕셔너리에 추가 가능
user['phone'] = '010-1234-1234'
print(user)

# user.clear()
# del user



print(" ")
print(" ")
#endregion


#region 집합
print(" ")
print(" ")

set1=set([1,2,3,4,5])
print(set1)
# set1=set([1,2,3,4,4,4,5]) # 중복이 안돼서 4는 한 개밖에 안 나옴

set2= set([4,5,5,5,5,6,7,8,4])

print(set1 & set2) # 교집합 intersection
print(set1.intersection(set2))
print(set1 | set2) # 합집합 union
print(set1 - set2) # 차집합 difference

set1.update([10,20]) # 추가해주기
print(set1)









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





#region 조건문 if
print(" ")
print(" ")
if 1==1:
    print("true")
    print("참")


x = 10
if x==10 :
    print('x는 10입니다')
else :
    print("x에 들어있는 숫자는")
print('10이 아닙니다')


score = 81
if score >= 90 :
    print('A학점 이네요')
elif score >= 80 :
    print('B학점 이시네요')
else :
    print('F ㅋㅋ')


str_value= str(123) #str_value = 123 이렇게 하면 수
if(str_value) :
    print(str_value)
else :
    print("문자열이 비어있소.")

list1=[5,6,6, "5g5g"] # or list1 = str()


if(list1) :
    print(list1)
else :
    print("리스트가 비어있네요")


x=10
y=20
if x==10 and y==20:         # & | 이런 기호들 안됨
    print(True)
else :
    print(False)

if not x==10:               # x^10 을 했는데 이건 안되는건가?
    print(True)
else:
    print(False)

x=15
if 10 <= x <20 :
    print('x가 10이상 20미만')
else:
    print('놉')


list1 = [1,2,3,4,5]

if 10 in list1:             # not in 형식도 가능
    print("10이 들어있소")
else:
    print("10이 없소")










print(" ")
print(" ")
#endregion


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



fund_money = input("가지고 싶은 돈은 얼마 인가요? ( 10만원 이상 ) : ")
fund_money = int(fund_money)
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













print(" ")
print(" ")