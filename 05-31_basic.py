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

name = "Tom"
age = 13

tt = f'{name} is {age} years old'
print(tt)

a = 10
b = 3
ab = a/b
tt2 = f'{a} / {b} = {ab:.6f}'
print(tt2)

# print("{<8}\nx{:<7}\n{:<8}" .format(2, 13, )) 문제 뭐였더라 PPT가 없다


# name = "banana"
# # type(name)
# # print(name.count('a')) # : 3
# # print(name.count('a', 0, 3)) # 0~3까지 a를 찾아서 몇 개인지 세줘 # : 1


# print(name.find('a', 2,4)) # 범위 : ana
# print(name.index('a'))


# print(name.upper())
# print(name.replace('a', 'c')) # 모두 바꿈 !
# print(name.replace('a', 'c', 2)) # 2개만 바꿈


# print(name.strip()) # 공백 짜르기
# print(name.rstrip()) # 오른쪽 공백 짜르기
# print(name.lstrip()) # 왼쪽 공백 짜르기


# split
name = "Life is too short, You Need python"
print(name.split()) # 아무것도 없으면 걍 공백으로 split 하게 됨
# ['Life', 'is', 'too', 'short,', 'You', 'Need', 'python']
name_list = name.split()

print(name.split(',')) # 지정해준 , 기준으로 split !
# ['Life is too short', ' You Need python']

print(name.split(' ', 2)) # 공백을 기준으로 2개만 split 해줘 !
# ['Life', 'is', 'too short, You Need python']
#    1개    2개         ㄴ ㅏㅁ ㅓㅈ ㅣ


# 언패킹
homepage = "구글 www.google.com"
site, host = homepage.split()
print(site, host)
# 구글 www.google.com

type(site)
# string
# type(site, host) 좀 이상함
# list



# value = input("입력") # 오우