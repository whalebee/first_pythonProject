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
    print('*arg의 타입은 :', type(args))
    # *arg의 타입은 : <class 'tuple'>
    max = 0
    for num in args:
        if num > max :
            max = num
    return max # 값도 출력해주게 됨        
max_num = get_max(10,20,1,2,50,32)
print(max_num)
# 함수안에 있는 print의 결과와 50이라는 값도 나옴

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










print(" ")
print(" ")