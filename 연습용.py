print(" ")
print(" ")

# ex1
age = input("나이를 입력해주세요 (만 나이, 7 이상 입력) :")
age = int(age)
# print(type(age))
money = 10000
# print(type(money))
print(f"현재 교통카드의 잔액은 {money}입니다.")

# 그러네 크게 하는게 낫겠네
if(age >= 19) :
    money -= 1250
elif(age >= 13) :
    money -= 1050
elif (age >= 7) :
    money -= 650
elif(age < 7):
    print("6세 이하는 무료입니다.")
else :
    print("잘못입력했습니다")
    exit()
    
print(f"남은 잔액 : {money}")



fund_money = input("가지고 싶은 돈은 얼마 인가요? ( 10만원 이상 ) : ")
fund_money = int(fund_money)
if(fund_money < 100000):  # 235800 이면? 4매, 3매, 1매, 1개, 3개
    print("기초 자금이 부족합니다. ")
    exit()
else:
    money_1 = fund_money // 50000
    fund_money = fund_money % 50000
    print(f"5만원권으로는 {money_1}매 나옵니다.")

    money_2 = fund_money // 10000
    fund_money = fund_money % 10000
    print(f"만원권으로는 {money_2}매 나옵니다.")

    money_3 = fund_money // 5000
    fund_money = fund_money % 5000
    print(f"오천원권으로는 {money_3}매 나옵니다.")

    money_4 = fund_money // 1000
    fund_money = fund_money % 1000
    print(f"천원권으로는 {money_4}매 나옵니다.")

    money_5 = fund_money // 500
    fund_money = fund_money % 500
    print(f"오백원으로는 {money_5}개 나옵니다.")

    money_6 = fund_money // 100
    fund_money = fund_money % 100
    print(f"백원권으로는 {money_6}개 나옵니다.")


# ex2 아이 잘못했넹
# fund_money = input("가지고 싶은 돈은 얼마 인가요? ( 10만원 이상 ) : ")
# fund_money = int(fund_money)
# if(fund_money < 100000):
#     print("기초 자금이 부족합니다. ")
#     exit()
# else:
#     choice = input("5만원권:1 , 만원권:2, 오천원권:3, 천원권:4, 오백원:5, 백원:6 이 중에서 고르세용 : ")
#     choice = int(choice)
#     if choice == 1:
#         money_1 = fund_money/50000
#         print(f"5만원권으로는 {int(money_1)}매 나옵니다.")
#     elif choice == 2:
#         money_2 = fund_money/10000
#         print(f"만원권으로는 {int(money_2)}매 나옵니다.")
#     elif choice == 3:
#         money_3 = fund_money/5000
#         print(f"5천원권으로는 {int(money_3)}매 나옵니다.")
#     elif choice == 4:
#         money_4 = fund_money/1000
#         print(f"천원권으로는 {int(money_4)}매 나옵니다.")
#     elif choice == 5:
#         money_5 = fund_money/500
#         print(f"500원으로는 {int(money_5)}개 나옵니다.")
#     elif choice == 6:
#         money_6 = fund_money/100
#         print(f"100원으로는 {int(money_6)}개 나옵니다.")
#     else :
#         print("지정된 숫자 이외의 다른 문자가 입력되었으니 종료합니다. 왜냐하면 반복문을 모르거든요")
#         exit()














print(" ")
print(" ")