print(" ")
print(" ")

# 클래스가 같은 객체들간의 계산
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






print(" ")
print(" ")