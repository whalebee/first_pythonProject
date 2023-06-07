print(" ")
print(" ")

# file = open("myFile.txt", "w")
# file.write("Life is too short")
# file.close()




# args = sys.argv[1:5]

# for value in args:
#     print(value)
# print(f"0번째는 {sys.argv[0]}")


# ex1 = open("word.txt", "r")
# ex1.close()

# with open("word.txt", "r") as file:
#     file.readlines()



# args1 = sys.argv
# for value in args1:
#     print(value)

# with open("word.txt", "r") as file:
#     content = file.readlines()
#     for line in content:
#         words = line.split()  
#         word_count = len(words)  
#         print(f"단어 개수: {word_count}")


# import sys
# with open("word.txt", "r") as file:
#     content = file.readlines()
#     count = 0
#     for line in content:
#         count += 1
#         print(line)

# print(count)



# ex1
count = 0
with open("word.txt", "r") as file :
    ex = file.read().split(',')
    for word in ex:
        count += 1
        if 'c' in word:
            print(word)
print(f"총 단어의 개수는 : {count}개")


# ex2
with open("grade.txt", "w") as grade_w :
    for i in range(10) :
        score = input(f"{i+1}번째 파이썬의 시험 점수 : ")
        grade_w.write(score + "\n")
    

# ex3
r_count = 0
sum = 0
with open("grade.txt", "r") as grade_r :
    for value in grade_r :
        r_count += 1
        sum += int(value)
        # print(value)
avg = sum / r_count
# print(f"총점은 : {sum}")
# print(f"평균은 : {avg}")

with open("result.txt", "w") as result :
    result.write(f"총점은 : {sum} \n")
    result.write(f"평균은 : {avg} \n")


print(" ")
print(" ")