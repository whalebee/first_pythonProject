print(" ")
print(" ")
#region lambda 과제
# b_days = input("생일을 입력하세요 ! mm/dd :").split(' ')

# # 8/15 1/11 3/1 -> 결과는 08월15일 1월11일 이런식으로

# print(lambda x : f"{0^b_days}", [b_days])

# test = list(map(data, b_days))

# result = ' '.join(test)



b_days = input("생일을 입력하세요 (형식 : mm/dd) :").split(' ')

# print(b_days)

la_date = lambda x : f"{x.split('/')[0]:0>2}월{x.split('/')[1]:0>2}일"
result = ' '.join(map(la_date, b_days))

print(result)



#endregion









#region 



#endregion








print(" ")
print(" ")