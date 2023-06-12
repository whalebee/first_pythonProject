print(" ")
print(" ")

# 구구단

def pan(str_a):
    if len(str_a) <= 1:
        return True
    if str_a[0] != str_a[-1]:
        return False
    return pan(str_a[1:-1])


print(" ")
print(" ")