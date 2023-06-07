print(" ")
print(" ")
class Person:
    count = 0 # 클래스 속성 -> 클래스 안에서 공통적으로 쓰는 변수 ( 모든 인스턴스에서 공유됨 )

    # 생성자 함수
    def __init__(self, name, age, address, wallet):
        # 인스턴스 속성(변수)
        self.name = name
        self.age = age
        self.address = address
        self.count = 0
        self.__wallet = wallet

        Person.count += 1

    @property
    def wallet(self):
        return self.__wallet
    
    @wallet.setter
    def wallet(self, wallet):
        if wallet < 0:
            print("입력 값 오류")
            return
        self.__wallet = wallet


kim = Person("김스나", 20, "an-san", 10000)
lee = Person("lee", 30, "seoul", 20000)

print(Person.count) # 클래스 속성 보는 것
print(kim.count) # 인스턴스 속성 보는 것
print(lee.count)













print(" ")
print(" ")