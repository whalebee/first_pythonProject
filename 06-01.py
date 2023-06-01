# ----------------------------------------------
# -----------------------------------------------------------------------------------------------
#region 인덱스 응용-1 & 문제
# 인덱스 응용
# nested_list2=["Hello!", [1,2,3], ["Hi Python", 4, [5,6,7]]]

# # 출력해야할 것들
# # Hello! Hi Python
# # 4,5

# a = nested_list2[2][1]
# b = nested_list2[2][2][0]

# print(nested_list2[0], nested_list2[2][0])
# print(f"{a},{b}")


# ----------------------------------------------
# # 출력해야할 것들
# 5,6
# Python

# print(nested_list2[2][2][:2])
# print(nested_list2[2][0][3:])
#endregion


#region 리스트 기본 & 문제
# list1 = [1, 2, 3]
# str(list1) + "Hi"   # 가능
# list1 + "Hi"      # 불가능
# print(list1*3) # 123 123 123 이렇게 3개


# list1 = [1,2,3]
# list2 = list1 + list("Hi")
# list3 = str(list1) + "Hi"
# print(list2)
# print(list3)


# my_list=[]
# # 추가
# my_list.append(1) 
# print(my_list)
# my_list.append(2)
# # [1, 2]

# # 삽입
# my_list.insert(1,3) 
# # [1, 3, 2] -> 1자리에 3이 넣어지고 그 뒤는 밀려남

# # 확장
# my_list.extend([4,5,6])
# # [1,3,2,4,5,6]

# # 추가로 리스트를 넣으면 [] 가 더 들어가짐 (중복)
# my_list.append([7,8])
# # [1,3,2,4,5,6, [7,8]]

# # 단순 연산 ( 대입이 아님 )
# my_list2 = [9,10]
# # print(my_list+my_list2)

# pop은 인덱스를 다룸
# my_list.pop()
#[7, 8]
# 그 다음 print my_list 해보면 [7,8]이 사라짐
# my_list.pop(1) 이러면 인덱스 1의 자리에 있는 3이 사라짐

# my_list.remove(1) # 인덱스가 아니라 value를 다룸
# print(my_list) 0의 자리에 있는 1 value가 사라짐

# 리스트 안의 값들이 사라짐
# my_list.clear()
# del my_list[:]

# 리스트 자체가 사라짐
# del my_list

# 특정범위만 지우기도 가능
# del my_list[:2]
# my_list[0:2] = []
# 같은 뜻

# # 실습
# my_list=[1,2,3,'a','b','c']
# # pop, remove, del, [] 각각 사용해서 지워보기

# # index를 기준으로 하는 pop
# print(my_list.pop())
# print(my_list)
# # [1, 2, 3, 'a', 'b']

# # remove는 value를 지우는거라 문자 지우고 싶으면 문자형식을 써줘야함
# print(my_list.remove('a')) 
# print(my_list)
# # [1, 2, 3, 'b']

# del my_list[:1]
# print(my_list)
# # [2, 3, 'b']

# my_list[:3] = []
# print(my_list)
# # []

# # 정렬
# my_list=[4,3,1,2,5]
# print(my_list.sort()) # [1,2,3,4,5]
# print(my_list.reverse()) # [5,4,3,2,1]
# print(my_list.sort(reverse=True)) # sort와 reverse를 한 번에 [5,4,3,2,1]


# # count 
# my_list3=['a','b','d','d']
# print(my_list3.count('d')) # 2 개수

# print(my_list3.index('d')) # 2 d가 있는 자리


# list1=[1,2,3]
# list2=list1
# list2[0] = 4
# print(list1, list2) # 주소를 참조해서 바꾸는 것 => 얕은 복사
# # [4,2,3] [4,2,3]

# # 둘 다 id가 같음 ! ( 같은 곳을 바라보기 때문 )
# print(id(list1)) 
# print(id(list2))

# list2 = list1.copy()
# list2[0] = 1
# print(list1, list2)
# # [4,2,3] [1,2,3]
# # 서로 id도 다름

# print(list2 = list1[:])
# print(list2 = list(list1))
# print([] + list1)


# # ?? 잤다
# list1=[1,2,3,[4,5]]
# import copy
# list2=copy.deepcopy(list1)

# fruit = ['strawberry','peach', 'banana', 'melon', 'orange']
# print(fruit[2:4], fruit[::2])
# # ['banana', 'melon'] ['strawberry', 'banana', 'orange']



# 딕셔너리


#endregion