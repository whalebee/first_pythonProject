# 1번
ex1 = input("문자열을 입력하세요 : ")
ex1_find = input("찾을 단어를 입력하세요 : ")
ex1_replace = input("바꿀 단어를 입력하세요 : ")
print("----- 결과 -----\n")
print(ex1.replace(ex1_find, ex1_replace))


# 2번
ex2 = input("주민등록번호를 입력하세요 : ")
# print(ex2.split('-'))
ex2_first, ex2_last = ex2.split('-')
print("앞자리는 : {0}\n뒷자리는 : {1}입니다.".format(ex2_first, ex2_last))


# 3번
ex3 = ex2_last[:1]
print(f"주등록번호의 성별을 나타내는 숫자는 {ex3}입니다. ")


# 4번
ex4_year = input("태어난 년도를 입력해주세요 [ex) 1993 ] : ")
ex4_month = input("태어난 월을 입력해주세요 [ex) 01 or 11 or 5 ] : ")
ex4_day = input("태어난 일을 입력해주세요 [ex) 01, 30 ] : ")

ex_4 = ex4_year + ex4_month
print(f"{ex4_year:^4}/{ex4_month:0>2}/{ex4_day:0>2}")


