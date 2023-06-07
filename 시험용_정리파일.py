print(" ")
print(" ")
#region 문자열 1번

# 문자열 자료형
a = 2
b = 13
test3 = "%8d \nx %6d\n--------\n%8d" % ( a, b, a*b)
test4 = "{0:>8} \nx {1:>6}\n--------\n{2:>8}" .format( a, b, a*b )
print(test3)
print(test4)

cnt = 3
test5 =         f"I Have [{cnt:#^10}] apples"
print(test5)    # I Have [####3#####] apples


#endregion



print(" ")
print(" ")