print(" ")
print(" ")







#region 클래스의 숫자 연산
class Grade:
    def __init__(self, score):
        self.score = score

    def __add__(self, num):
        self.score += num
        # return self.score + num

my_grade = Grade(50)

my_grade + 10 # __add__가 없으면 오류가 남
print(my_grade.score)

# print(dir(object))



#endregion








#region 클래스에 속한 객체들의 연산 개념
class Grade:
    def __init__(self, score):
        self.score = score

    def __add__(self, other):
        # Feedback : self는 Grade 클래스니까 self는 체크하지 않아도 돼
        # if(isinstance(self, Grade) & isinstance(other, Grade)):
        if(isinstance(other, Grade)):
            result = self.score + other.score
        else :
            raise TypeError("Grade 외의 객체와의 덧셈 불가")
        return result

class test:
    def __init__(self, score):
        self.score = score

math_score = Grade(50)
science_score = Grade(80)
test_score = test(30)

print(math_score + science_score) # 같은 클래스로 계산 가능
# print(math_score + test_score) # 클래스가 달라서 오류
# print(math_score + 10) # 마찬가지로 오류


#endregion







#region 클래스 연산 예제
class HouseGrant:
    def __init__(self, name):
        self.name = name + 'Grant'
        self.check_marry = 0
        self.loving = 0

    def travel(self, location):
        print(f"{self.name} traveled to {location}")

    def love(self, target):
        print(f"{self.name} and {target} loved")
        self.loving = 1

    def __add__(self, other):
        if((not isinstance(other, HouseGrant)) & self.loving == 1):
            if(self.check_marry == 1):
                return 1
            print(f"{self.name} and {other.name} were married")
        else :
            print(f"{self.name}와(과) {other.name}은(는) 같은 집안임 큰일남")
            return 0
            # raise TypeError("같은 집안임.. 큰일남")
        
    def fight(self, other):
        self.check_marry = 1
        if((not isinstance(other, HouseGrant)) & (self + other)):
            print(f"{self.name} and {other.name} fought")
        else :
            print("같은 집안 사람이거나 사랑하는 사이가 아님")

    def __sub__(self, other):
        if (self + other):
            print(f"{self.name} and {other.name} are divorced")
        else:
            print(f"{self.name}와(과) {other.name}은(는) 사랑하는 사이가 아니다 !")

class HouseB:
    def __init__(self, name):
        self.name = name + 'B'

    def __str__(self):
        return f"{self.name}"

    def travel(self, location, date):
        print(f"{self.name} traveled to {location} for {date} days")

# class forCheck:
#     def __init__(self, name):
#         self.name = name

hue = HouseGrant('Hue')
suzi = HouseB('suzi')
# test1 = forCheck('test1')
# test2 = HouseGrant('test2')

hue.travel('Paris')

suzi.travel("Paris", 3)

hue.love(suzi)

hue + suzi
# hue + test2 
# 같은 집안 테스트 필요 -ch

hue.fight(suzi)
# hue.fight(test1) # 같은 집안이거나 -ch
# hue.fight(test2) # 사랑하는 사이가 아니거나 테스트 필요 -ch

hue - suzi
# 사랑 하는 사이가 아닌 것 확인 필요
# hue - test1 # 같은 집안이 아님 -ch
# hue - test2 # ㅎㅎ

# print(dir(HouseGrant)) 




#endregion








#region 예외처리 기본개념
def dev(m,n):
    try:
        result = m/n
    except ZeroDivisionError as e:
        return f"0으로 못 나눠: {e}"
    except TypeError:
        return "숫자를 입력해"
    # 이렇게 합치는 것도 가능
    # except (ZeroDivisionError, TypeError):
    #     return "입력오류"
    except Exception as e:
        print(f"오류: {e}")
    return result

print(dev(10,0)) # 0으로 못 나눠
print(dev(10,'a')) # 숫자를 입력해



def read_file(file_name):
    try:
       # 실행구문 : 이 구역에서 발생한 예외만 처리할 수 있다.
       file = open(file_name, "r")
    except Exception as e:
        # 예외구문 : 발생한 예외처리
        print(e)
    else :
        # 예외가 발생하지 않았을 경우
        print("else")
        print(file.readline())
        file.close()
    finally:
        # 예외 발생여부와의 관계없이 실행해야하는 처리
        print("곡 해야하는 처리. 리소스 클로즈 등")

read_file("test.txt")    


def dev(m,n):
    try:
        if m < n:
            # pass # 걍 지나감
            raise ValueError # 강제로 만듦
        else :
            result = m / n
            return result
    except ValueError:
        print("m이 더 작다")

    
class MyError(Exception):
    def __str__(self):
        return "사용자 생성 예외입니다."
    
def mul(m, n):
    if m < n :
        raise MyError
    

mul(5, 10)


#endregion








# region 예외처리 예제
# ex1
class FourCalc:

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

class CheckFourCalc(FourCalc):
    def div(self):
        try:
            super().div() # 피드백 받은 곳
        except ZeroDivisionError:
            return "오류 발생 : division dy zero"


myCalc = CheckFourCalc()
myCalc.setdata(10,0)
print(myCalc.add())
print(myCalc.sub())
print(myCalc.mul())
print(myCalc.div())








# ex2
class Person:
    def __init__(self, name, phone, gender="N", age = 0):
        self.name = name
        self.__age = age
        self.phone = phone
        self.gender = gender
        
    def __str__(self):
        return f"이름:{self.name}, 나이:{self.__age}, 전화번호:{self.phone}, 성별:{self.gender}"
    
    # def age_start_end(value):
    #     def wrapper(self, age):
    #         print(value.__name__, "함수 시작")
    #         if age < 0:
    #             print("입력 값 오류")
    #             return
    #         result = value(self, age)
    #         print(f"입력된 나이 : {result}")
    #         print(value.__name__, "함수 정상 종료")
    #         return result
    #     return wrapper
    
    # @age_start_end
    # age = property(get_age, set_age)
    # 2번째 방법으로 하라는 뜻
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 0:
            print("입력 값 오류")
            raise ValueError
            # return
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


yone = Person("yonezu kenshi", "010-1234-1234", "M")
yone.age = -31
print(yone)


#endregion








print(" ")
print(" ")