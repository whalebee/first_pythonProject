print(" ")
print(" ")

# ex5
# 재귀함수 아닌 버전
# def palindrome(str_a):
#     str_a = str_a.replace(" ", "")
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
        
# 재귀함수 버전
def palindrome(str_a):
    # str_a = str_a.replace(" ","")
    # print(str_a[1:-1])
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











print(" ")
print(" ")