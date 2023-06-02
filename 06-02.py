#region 
print(" ")
print(" ")

# prompt = """1.Add \n2.Del\n3.List\n4.Quit\nEnter Number : """

# 내가 해서 틀린 거
# num = 0
# while num < 4 :
#     print(prompt, int(input(num)))
#     print(num)
    
# 선생님 버전
# while int(input(prompt)) != 4 :
#     pass # 괄호가 없을 때 그냥 pass 써주면 됨 !


grade = 'F'
score = int(input("성적입력 : "))

# 점수 입력했을 때 들어와서 검사를 해야할 듯?
# 잘 입력했으면 끝나야하고
# 잘못 입력했으면 계속 돌아야하고? -> 애초에 잘입력했어도 while문안에는 들어가야한단말이지?
# 뭔가 지저분한데 ㅋㅋ
# 내가 한 버전
while (score < 0 or score > 100) :
    print("잘못된 입력입니다 다시 입력해주세요")
    score = int(input("성적입력 : "))

if 0 < score < 101 :
    if score >= 90 :
        grade = 'A' 
    elif score >= 80 : 
        grade = 'B' 
    elif score >= 70 : 
        grade = 'C' 
    elif score >= 60 : 
        grade = 'D' 
    elif score < 60  : 
        grade = 'F' 

print("{}점은 {}학점입니다." .format(score, grade))












print(" ")
print(" ")
#endregion


#region while문 예제
print(" ")
print(" ")


# print(type(n)) 

# *
# **
# ***
# ****
# *****
# 5번을 반복해야한다 가정했을 때
# 결국 행과 열을 위해 2번씩 써야함 -> 아니라넹 ~ -> 아니넹 ~

n = int(input("몇 단짜리 별이 보고 싶어요? : "))
i = 0
j = 0

while(i <= n) :
    print("*" * i)
    i += 1
 

print(" ")
print(" ")

# 거꾸로 하려면? 위에서부터 내려오면 됨
i = n
while( i >= 0 ):
    print("*" * i)
    i -= 1


print(" ")
print(" ")
#endregion





#region while문 예제 2번 커피자판기
print(" ")
print(" ")

# 커피 10잔이 한도
# 커피 1잔 = 300원
# 돈을 입력했을 때 그 외의 돈을 다시 돌려줘야한다.
# 남은 커피의 양 출력도 해야하고
# 커피를 모두 팔면 판매중지


# 돈을 넣어주세요

# 거스름돈 있을 때
# 거스름돈 200을 주고 커피를 줍니다 ->  커피 개수 차감
# 커피 잔고 출력


# 다시 돈을 넣어주세요

# 거스름돈 없을 때
# 커피를 줍니다 -> 커피 개수 차감
# 커피 잔고 출력


# 다시 돈을 넣어주세요
# 돈이 모자를 때
# 돈을 다시 돌려주고 커피를 주지 않는다 -> 개수 일정
# 커피 잔고 출력

# 커피 원해?

coffee = 10

# 커피가 1잔 이상 있을 때 계속 판매
while(coffee > 0) :
    money = int(input("돈을 넣어 주세요 : "))

    if (money < 300) :
        print("돈이 부족합니다.")
    elif (money == 300) :
        print("커피 한 잔을 드립니다.")
        coffee -= 1
    else :
        # 3000원을 주든 30000원을 주든 한 잔만 파는 중 ( 자판기라서 )
        change =  money - 300
        print(f"거스름돈 {change}원을 드리고 커피를 한 잔 드립니다.")
        coffee -= 1
        
    print(f"남은 커피의 수량은 {coffee}잔 입니다.")

print("커피가 모두 판매되었습니다. \n판매를 종료합니다 ^ㅡ^")


print(" ")
print(" ")
#endregion





#region 반복문 (1)
print(" ")
print(" ")

# print(list(range(1,6)))

for value in range(1,6):
    print(value, end=" ")
# 1 2 3 4 5
print("")
for value in range(5,0,-1):
    print(value, end=" ")
# 5 4 3 2 1

total = 0
score_list = [95,100,80,90,77]

for score in enumerate(score_list):
    print(score)
# 인덱스 자리도 같이 나옴

for i, score in enumerate(score_list):
    print(f"{i+1}번째 점수는 {score} 입니다.")
    total += score

print(f"총점은 {total} 입니다.")


grade = {"이름":"danaka", "학년":"3", "성적":"A"}
# print(grade.keys())
# print(grade.values())
# print(grade.items())

# for item in grade:
#     print(item)
# # 이름 학년 성적


# 같은 것임 ( 표현만 다를 뿐 )
for key, value in grade.items():
    print("key: "+ key, "value: "+value)

# for key, value in grade.items():
#     print("key:", key, "value:",value)






print(" ")
print(" ")


#endregion







#region 



#endregion