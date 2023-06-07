print(" ")
print(" ")
#region lambda 과제
# b_days = input("생일을 입력하세요 ! mm/dd :").split(' ')

# # 8/15 1/11 3/1 -> 결과는 08월15일 1월11일 이런식으로

# print(lambda x : f"{0^b_days}", [b_days])

# test = list(map(data, b_days))

# result = ' '.join(test)



b_days = input("생일을 입력하세요 (형식 : mm/dd) :").split(' ')

# print(b_days)

la_date = lambda x : f"{x.split('/')[0]:0>2}월{x.split('/')[1]:0>2}일"
result = ' '.join(map(la_date, b_days))

print(result)



#endregion









#region 파일 입출력
print(" ")
print(" ")
# ex1
count = 0
with open("word.txt", "r") as file :
    ex = file.read().split(',')
    for word in ex:
        count += 1
        # 3가지의 방법
        # if word.find("c") >= 0 :
        # if workd.count('c) > 0 :
        if 'c' in word:
            print(word)
print(f"총 단어의 개수는 : {count}개")


# ex2
with open("grade.txt", "w") as grade_w :
    for i in range(10) :
        score = input(f"{i+1}번째 파이썬의 시험 점수 : ")
        grade_w.write(score + "\n")
    

# ex3
r_count = 0
sum = 0
with open("grade.txt", "r") as grade_r :
    # 다른 방법
    # lines = grade_r.read().split('\n')
    # for line in lines:
    #     if line :
    #         sum += int(line)

    # 내가 한 방법
    for value in grade_r :
        r_count += 1
        sum += int(value)
        # print(value)
avg = sum / r_count
# print(f"총점은 : {sum}")
# print(f"평균은 : {avg}")

with open("result.txt", "w") as result :
    result.write(f"총점은 : {sum} \n")
    result.write(f"평균은 : {avg} \n")


# 이런식으로도 사용가능
# with open(file, 'r') as file_r, open(file, 'w') as file_w


print(" ")
print(" ")


#endregion








#region class와 instance 기본
a = "hi"
print(isinstance(a, str))
# True

class Person:
    pass
tanaka = Person()
print(isinstance(tanaka, Person))
# True


def factorial(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(-1)) # 오류를 방지했음
print(factorial(1.2)) # 오류를 방지했음



#endregion








#region class와 property, 보안성을 가진 객체안의 변수, 메서드, 데코레이터
print(" ")
print(" ")
print("--기초--")
class Person_basic:

    # 기초
    def greeting(self, v1, v2, *args):
        print("Hello", v1, v2)
        for value in args:
            print(value)

# 기초
tanaka = Person_basic() # 생성자함수
tanaka.greeting("Python", "C", [1,2,3,4,5]) # Hello Python C [1,2,3,4,5]


print("")
print("--응용--")

class Person:
    # 오버로딩은 파이썬에서 불가능함
    # def __init__(self):
    #     self.name = "noname"

    # 생성자 메서드 ( 객체를 만들 때 자동으로 호출 됨 )
    # 초기값을 마지막에 지정해줘야한다는 것 !
    def __init__(self, age, address, name="Noname"):
        # print("생성자함수")
        self.hello = "하이용 :D"
        self.name = name
        self.age = age
        self.address = address

    # 응용
    def greeting2(self):
        print(f"{self.hello} 저는 {self.age}살 {self.name}이고, {self.address}에 살고 있습니다.")

# 응용
tanaka = Person("tanaka", 31, "경기도")
lee = Person("lee", 31, "시흥시")
yoho = Person(31, "마곡동")

tanaka.greeting2() # 하이용 :D 저는 31살 tanaka이고, 경기도에 살고 있습니다.
lee.greeting2() # 하이용 :D 저는 31살 lee이고, 시흥시에 살고 있습니다.
yoho.greeting2() # 하이용 :D 저는 31살 Noname이고, 마곡동에 살고 있습니다.


# 클래스가 비어있는 상태로 정의화되었을 때
print("")
print("")
print("--empty--")
class Person_1:
    pass
tanaka = Person_1()
tanaka.name = '다나카'
print(tanaka.name) # 다나카

sakura = Person_1()
# print(sakura.name) # 원래는 없다는 것을 증명하기 위함


print("")
print("")
print("--보안성--")
# 보안성
class seceret:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address= address
        self.__wallet = wallet # 숨기기

    def pay(self, amount):
        self.__wallet -= amount

    def balance(self):
        print(f"현재 잔액은 {self.__wallet}원입니다")

    def get_wallet(self):
        return self.__wallet
    
    def set_wallet(self, wallet):
        if wallet < 0:
            print("입력 값 오류")
            return
        self.__wallet = wallet # 0 보다 크면 여기와서 저장
    
    wallet = property(get_wallet, set_wallet)
    # 월렛을 사용하면 get_wallet이나 set_wallet 둘 다 사용하게 만드는 함수 -> property


tanaka = seceret('tanaka', 25, 'Tokyo', 10000)
# print(tanaka.name) # 가능
# print(tanaka.__wallet) # 나오지 않음 ! 보안으로 없애버리는 것처럼 숨김
tanaka.balance() # 이건 가능

print(tanaka.get_wallet())
print(tanaka.wallet) # property 사용
tanaka.wallet = -1000 # 입력 값 오류


print("")
print("")
print("--property--")
class Person_perty:
    # 아니면 이렇게 써도 됨
    @property
    def wallet(self):
        return self.__wallet
    
    @wallet.setter
    def wallet(self, wallet):
        if wallet < 0:
            print("입력 값 오류")
            return
        self.__wallet = wallet


print("")
print("")
print("--데코레이션--") # 시험에 정의만 나옴 ( 무엇인지만 알면 됨 )
def print_start_end(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, "함수 시작")
        result = func(*args, **kwargs) # 실제 함수는 여기서 작용
        print(func.__name__, "함수 끝")
        return result

    return wrapper

@print_start_end # def에 들어가서 ... 모름
def hello():
    print("Hello")

hello()
# hello 함수 시작
# Hello
# hello 함수 끝


def score():
    print("score")
score()
# score


# 매개변수와 return값이 있기때문에
# 위에 result와 return을 추가해줬음
@print_start_end
def add(a,b):
    return a+b

print(add(10,20))
# add 함수 시작
# add 함수 끝
# 30 # 함수가 끝이 나고나서 print를 해줬기때문에 함수 끝 밑에 출력된 것











print(" ")
print(" ")
#endregion








#region 



#endregion





print(" ")
print(" ")