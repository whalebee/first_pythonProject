print(" ")
print(" ")

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
        for x,y in self.score.items():
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



print(" ")
print(" ")