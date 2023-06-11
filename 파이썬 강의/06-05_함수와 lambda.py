print(" ")
print(" ")

#region 함수의 정의 방법
print(" ")
print(" ")

# 매개 변수가 없는 함수 정의
def hello():
    print("Hello")
# print(hello())


# 매개 변수 존재하는 함수 정의
def hello2(value1):
    print(f"{value1} Hello~")
# print(hello2('haha'))


# 전달받은 두 수를 더해서 출력하는 함수 정의
def ex(value1, value2) :
    '''전달받은 두 수를 더해서 출력하는 함수 정의'''
    print(f"{value1} + {value2} = {value1 + value2}")
print(ex(3, 5))
print(ex("Hello~ ", "Python"))
print(ex.__doc__) # 전달받은 두 수를 더해서 출력하는 함수 정의
# help(ex) 이렇게도 볼 수 있어 !
# print(help(ex))



# 리턴 값이 있는 함수 정의 -> 걍 return 쓰면 됨
def fn_sum(v1, v2):
    return v1+v2
print(fn_sum(5,8))
# 13

# 리스트를 매개변수로 던져주려면? -> *리스트이름
list_test = [10, 20]
print(fn_sum(*list_test)) 
# 30


# 가변 매개변수
# def 함수이름(*arg): -> tuple형식으로 전달
def get_max(*args):
    print('*args의 타입은 :', type(args))
    # *args의 타입은 : <class 'tuple'>
    max = 0
    for num in args:
        if num > max :
            max = num
    return max # 값도 출력해주게 됨        
max_num = get_max(10,20,1,2,50,32)
print(max_num)
# *args의 타입은 : <class 'tuple'>
# 50

# def 함수이름(**arg): -> dictionary형식으로 전달
def show_args(**args):
    print('**args의 타입은 :', type(args))
    keys = args.keys()
    for key in keys:
        print("key:", key, "/", "value:",args[key])

print(show_args(name='tanaka', age=30, address='Tokyo'))
# 이런식으로 순서를 바꿔줘도 가능해짐
# 일치하는 곳에 알아서 넣어주기 때문
print(show_args(age=30, address="Tokyo", name="tanaka"))

# 함수의 초기값 설정 !
# 초기값은 마지막에서부터 써야함
def show_args(name, age, address="nagoya"):
    print(f"{name}, {age}, {address}")
print(show_args("tanaka", 30, "Tokyo")) # tanaka, 30, Tokyo
print(show_args("tanaka", 30)) # tanaka, 30, nagoya ( 없는 매개변수는 초기값으로 설정된 값이 나오게 됨)


# 함수에서 여러 값을 리턴해주기 -> unpacking 사용
# 일반
def check_return():
    return "Hello", 100

result = check_return()
print(type(result))
# <class 'tuple'>

v1, v2 = check_return()
print(v1) # Hello
print(v2) # 100

# 튜플
v3 = check_return()
print(v3) # ('Hello', 100) 튜플이지 !
v4 = list(check_return())
print(v4) # ['Hello', 100] 이러면 리스트고ㅋㅋ
# 아니면 함수 정의하는 곳 return 에서 리스트로 만들어줘도 됨

# 리스트
def check_list_return():
   return ["Hello", 100]

# 딕셔너리
def check_di_return():
    return {"v1": "Helloooo", "v2" : 100}
di_result = check_di_return()
print(di_result)
# {'v1': 'Helloooo', 'v2': 100}






print(" ")
print(" ")
#endregion








#region 함수 사용할 때 전역변수 사용하기
print(" ")
print(" ")

from pprint import pprint

phone_book = [{"name":"KIM", "phone":"010-111-1111"},
              {"name":"LEE", "phone":"010-222-2222"}
              ]

count = 2

def add_phone_book(name, phone):
    # count를 이렇게 하지 않으면 오류남
    global count # 함수 안에서 전역변수를 쓰겠다고 선언하는 것
    count += 1
    phone_book.append({"name":name, "phone":phone})

add_phone_book("park", "010-333-3333")
print(count)
pprint(phone_book)


print(" ")
print(" ")



#endregion








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








#region lambda(람다) 사용
print(" ")
print(" ")

lambda_add = lambda x,y : x+y
print(lambda_add(10,20))
# 30

my_list=[lambda x,y : x+y, lambda x,y : x*y]
print(my_list[0](3,4)) # 7 
print(my_list[1](3,4)) # 12



# map -> 앞에 있는 요소(함수)를 뒤에있는 애들에게 각각 적용시켜줌

# lambda 형
print(list(map(lambda x : x+10, [1,2,3]))) # [11, 12, 13]

#lambda와 list 사용
list_a = [1,2,3]
print(list(map(lambda x : x+10, list_a))) # [11, 12, 13] 

# lambda 없이
def plus10(x):
    return x+10
result = list(map(plus10, [1,2,3]))
print(result) # [11, 12, 13] 


# 일반 append로 사용
def c_square(list_a):
    list_b = []
    for i in list_a:
        list_b.append(i*i)
    return list_b
list_result = [4,5,6]
print(c_square(list_result)) # [16, 25, 36]

# map 사용
def c_square_2(target):
        return target*target
print(list(map(c_square_2, list_result))) # [16, 25, 36]

# map과 lambda 사용
print(list(map(lambda x : x*x, list_result))) # [16, 25, 36]


print(" ")
print(" ")
#endregion








#region filter와 lambda 사용(2)
print(" ")
print(" ")


# filter
def fn_filter(x):
    return 5 < x < 10
result = list(filter(fn_filter, [5,6,7,8,9,10]))
print(result) # [6, 7, 8, 9]

# lambda 식으로 바꾸면?
result_l = list(filter(lambda x : 5<x<10, [5,6,7,8,9,10]))
print(result_l) # [6, 7, 8, 9]


print(list(map(lambda x : x+10, [1,2,3])))
# [11, 12, 13]

print(list(map(lambda x: str(x) if x%2==0 else x, [1,2,3])))
# [1, '2', 3]





print(" ")
print(" ")


#endregion












print(" ")
print(" ")