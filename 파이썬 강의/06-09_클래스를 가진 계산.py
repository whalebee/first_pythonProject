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








#region 



#endregion










print(" ")
print(" ")