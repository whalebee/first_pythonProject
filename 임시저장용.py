print(" ")
print(" ")

# ex1
# 함수 정의
def ex1(*args) :
    result = 0
    for value in args:
        result += value

    return result

# 매개변수 설정
ex1_sum = ex1(3, 5, 8)

# 결과 확인
print(f"1번문제 : {ex1_sum}")




# ex2 -> 내장함수 사용하여 최대값, 최소값 구하기
list_ex2 = [52,273,103,32,57]
# print(min.__doc__)
print(f"2번문제 최소값 : {min(list_ex2)}")
print(f"2번문제 최대값 : {max(list_ex2)}")




# ex3
def custom_min(*args):
    min = args[0]
    for x in args:
        if x < min:
            min = x
    return min

list_3_min = custom_min(10, 30, 40 ,50 ,60 ,70, 3, -5)
print(f"3번문제 커스텀 최소값 : {list_3_min}")

def custom_max(*args):
    max = 0
    for x in args:
        if x > max:
            max = x
    return max
list_3_max = custom_max(10, 30, 40, 50, 60, 70)
print(f"3번문제 커스텀 최대값 : {list_3_max}")



# ex4
def divide(x, y):
    quotient = x // y
    remainder = x % y
    # print(f"{x} // {y} = {x // y} (몫)") # 몫
    # print(f"{x} % {y} = {x % y} (나머지)") # 나머지
    return quotient, remainder
# print(f"4번문제 : {divide(10, 6)}")
v1, v2 = divide(10, 6)
print(f"4번문제 몫은 : {v1}")
print(f"4번문제 나머지는 : {v2}")




# ex5
# 재귀함수 아닌 버전
# def palindrome(str_a):
#     str_a = str_a.replace(" ", "") # 공백 제거 ( 띄어쓰기 때문에 )
#     count = 0
#     p = 0
#     m = -1
#     for v in str_a:
#         if str_a[p] == str_a[m]:
#             count += 1
#         # print(str_a[p])
#         # print(str_a[m])
#         p += 1
#         m -= 1
#     if ( count == len(str_a)):
#         return True
#     else:
#         return False
        
# 재귀함수 버전 -> 맞는데 최적화 필요
# def palindrome(str_a):
#     str_a = str_a.replace(" ","") 

#     def palindrome_re(str_a, first, last):
#         if first >= last:
#             return True
#         elif str_a[first] != str_a[last]:
#             return False
#         else:
#             return palindrome_re(str_a, first + 1, last - 1)

#     return palindrome_re(str_a, 0, len(str_a) - 1) # 인덱스의 범위때문에 -1 해줘야됨
        

def palindrome(str_a):
    # str_a = str_a.replace(" ","")
    print(str_a[1:-1])
    if len(str_a) <= 1:
        return True
    if str_a[0] != str_a[-1]:
        return False
    
    return palindrome(str_a[1:-1])





print(palindrome("역삼역")) # True
print(palindrome("12345678987654321")) # True
print(palindrome("123454231")) # False
print(palindrome("repaper")) # True
print(palindrome("다리 그리고 저고리 그리다")) # True
print(palindrome("다리 그리고 저고라 그리다")) # False
print(palindrome("1 2 321")) # True
print(palindrome("was it a cat i saw")) # True



