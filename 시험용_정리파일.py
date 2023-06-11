print(" ")
print(" ")
#region 문자열 1번

# 문자열 자료형
a = 2
b = 13
test3 = "%8d \nx %6d\n--------\n%8d" % ( a, b, a*b)
test4 = "{0:>8} \nx {1:>6}\n--------\n{2:>8}" .format( a, b, a*b )
print(test3)
print(test4)

cnt = 3
test5 =         f"I Have [{cnt:#^10}] apples"
print(test5)    # I Have [####3#####] apples







print("[{0:>10}] 오른쪽정렬\n[{0:<10}] 왼쪽정렬\n[{0:^10}] 가운데정렬".format("정렬"))


print("{0}, {0}, {0}" .format("gg"))


cnt = 3
print (f"I Have [{cnt:#^10}] apples")







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
print(my_list+my_list2)







my_list = [1,2,3,'a','b','c']
# 4가지 방법을 사용해 'b' 제거하기
# pop, remove, del, [:]
my_list.pop(-2)
print(my_list)

my_list = [1,2,3,'a','b','c']
my_list.remove('b')
print(my_list)

my_list = [1,2,3,'a','b','c']
del my_list[4:5]
print(my_list)

my_list = [1,2,3,'a','b','c']
my_list[4:5] = []
print(my_list)







# 깊은 복사와 얕은 복사

# 리스트 내부의 객체 주소를 똑같이 바라보고 있는 경우 -> 얕은 복사가 진행됨
list1 = [1,2,3,[4,5]]
list2 = list1.copy()
list2[3][0] = 6
print(list1, list2)
# 해결방법은 import copy로 깊은 복사를 하면 된다.
# list2 = copy.deepcopy(list1)


# 리스트 내부에 객체가 없고 리스트를 복사해온 경우
list1=[1,2,3]
list2 = list1.copy()
list2[0] = 4
print(list1, list2)





# 튜플의 더하기
# 곱하기, 인덱싱, 슬라이싱은 리스트와 같음
tuple = (1,2,3)
tuple = tuple + (4,)
print(tuple)





# range함수
print(range(5))             # range(0, 5)
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(1,10)))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))  # [1, 3, 5, 7, 9]
print(list(range(10,1,-2))) # [10, 8, 6, 4, 2]


# enumerate
total = 0
score_list = [95, 100, 80, 90, 77]
for score in enumerate(score_list):
    print(score)
# (0, 95)
# (1, 100)
# (2, 80)
# (3, 90)
# (4, 77)


# 구구단
result = [ x * y for x in range(2, 10) if x % 2 == 1 for y in range(1, 10)]
print(result)


# 팩토리얼 재귀함수 -> 인스턴스 확인
def factorial(x):
    if not isinstance(x, int) or x < 0:
        return None
    if x == 1:
        return 1

    return x * factorial(x-1)



#endregion




# class 상속
class Person:
    def greeting(self):
        print("Person입니다 하이 ~")

class Grade:
    def greeting(self):
        print("Grade입니다 하이 ~")
    def score(self):
        print("학점을 관리합니다.")


# Student 클래스가 Person 이라는 클래스를 상속받음
# Person, Grade로 선언이 되어있으니
# 중복된 메서드 중에서 본인 클래스가 가장 우선 순위를 가지고
# 그 다음은 선언된 순서로 가진다 ( ex. Person (1) -> Grade (2) )
# 그래서 밑에 예시에서 greeting은 Person클래스에 있는 greeting 메서드를 쓰게 된다.
class Student(Person, Grade):
    def study(self):
        print("공부하쟈 !")

    # 부모 클래스가 가지고 있는 것과 같은게 있으면
    # 해당 클래스 안에 있는 것이 더 우선 순위를 가짐
    # def greeting(self):
    #     print("Hello")

    def greeting(self):
        super().greeting()  # 이것도 쓰고
        Grade.greeting(self)# 이것도 쓰고
        print("Hello")      # 이것도 쓰고ㅋㅋ
    # 이렇게 하면 3개를 다 쓰는 것

lee = Student()
lee.study()
lee.greeting() # 이렇게 상속받아서 greeting 메서드가 사용가능해짐



# 상속 예제
# ex1
class Person:
    def __init__(self, name, phone, gender="N", age = 0):
        self.name = name
        self.__age = age
        self.phone = phone
        self.gender = gender
        
    def __str__(self):
        return f"이름:{self.name}, 나이:{self.__age}, 전화번호:{self.phone}, 성별:{self.gender}"
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 0:
            print("입력 값 오류")
            return
        self.__age = age # 0 보다 크면 여기와서 저장
    
    def greeting(self):
        print(f"안녕하세요. {self.name}입니다.")

    def add_age(self):
        if(self.__age == 0):
            print("나이가 입력되어있지 않습니다.")
            return
        else:
            print(f"나이 추가 : {self.__age} + 1 = {self.__age + 1}")
            self.__age += 1

    def change_phone(self, new_number):
        self.phone = new_number


class Student(Person):
    def __init__(self, name, phone, gender="N", age=0):
        super().__init__(name, phone, gender, age)
        self.score = {}
        self.result_total = 0
        self.call_total = 0
        self.iscall_total = 0
        self.result_avg = 0

    def __str__(self):
        print(f"학생정보 : {super().__str__()}")
        return f"성적기록 : {self.score}"
    
    def add_subject(self, subject, score):
        if subject in self.score:
            print(f"{subject} 과목의 점수 갱신 ! ")
        self.score[subject] = score
    
    def total_score(self):
        self.iscall_total = 1
        for x,y in self.score.items(): # values() 로 뽑으면 더 간단
            self.result_total += y
            # print(y)
        print(f"총 점수 : {self.result_total}점")
        # return self.total

    def average_score(self):
        if self.iscall_total == 1:
            call_total = self.result_total
        else:
            call_total = self.total_score()
        result_avg = call_total / len(self.score)
        # print(call_total)
        print("평균 점수는 : {0:.2f}" .format(result_avg))
        # print(f"평균 점수는 : {result_avg:.2f}")

yone = Student("yonezu kenshi", "010-1234-1234", "M")
yone.age = 31
yone.add_subject("C", 80)
yone.add_subject("C", 98) # 과목 갱신
yone.add_subject("Python", 90)
yone.add_subject("Network", 80)
yone.add_subject("Linux", 60)
yone.add_subject("Maria_DB", 70)
yone.add_subject("Maria_DB", 90) # 과목 갱신
print(yone)
# yone.total_score()
yone.average_score()





# ex2
class FourCalc:
    # v1 = 0
    # v2 = 0

    def setdata(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2
    
    def sub(self):
        return self.v1 - self.v2
    
    def mul(self):
        return self.v1 * self.v2
    
    def div(self):
        return self.v1 / self.v2


class MoreFourCalc(FourCalc):
    def __init__(self, v1, v2):
        self.v1 = v1 
        self.v2 = v2

    def square(self):
        result = 1
        for x in range(self.v2):
            result *= self.v1
        return result

cal3 = MoreFourCalc(2, 16)
print(cal3.square())
print(cal3.add())
print(cal3.sub())
print(cal3.mul())
print(cal3.div())

























print(" ")
print(" ")