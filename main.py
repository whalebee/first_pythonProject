name = "Tom"
age = 13
test = "%s is %d years old" % (name, age)
# print(test)

a = 10
b = 3
test2 = "%d / %d = %f" % (a, b, a/b)
# print(test2)

a = 2
b = 13
test3 = "%8d \nx %6d\n--------\n%8d" % ( a, b, a*b)
# print(test3)



# "{2}의 {0}점수는 {1}점 입니다." .format('C', 50, "Python")


test3 = "{0:>8} \nx {1:>6}\n--------\n{2:>8}" .format( a, b, a*b )
# print(test3)

# count = 3
# f"I Have [{count:#^10}] apples"

print(" ")

NAME = "Tom"
AGE = 13

tt = f'{NAME} is {AGE} years old'
print(tt)

A = 10
B = 3
AB = a/b
tt2 = f'{A} / {B} = {AB:.6f}'
print(tt2)

# print("{<8}\nx{:<7}\n{:<8}" .format(2, 13, )) 문제 뭐였더라 PPT가 없다


NAME = "banana"
# type(name)
# print(name.count('a')) # : 3
# print(name.count('a', 0, 3)) # 0~3까지 a를 찾아줘 # : 1


print(NAME.find('a', 2,4)) # 범위 : ana
print(NAME.index('a'))

