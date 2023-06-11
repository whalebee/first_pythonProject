print(" ")
print(" ")


# import game_06_09.sound.echo as game_echo
# print(game_echo)

# # from game_06_09.sound import *    # 이렇게 모듈을 모두 쓰고 싶은데 안되니까 __init__ 모듈을 쓰는 것
# from game_06_09.sound import *      # __init__ 설정 후 가능
# print(echo)
# wav.wav_test()


# from random import *
# # print(random.__all__)  # 없다 !

from game_06_09 import sound
import game_06_09
# sound init에서 import echo와 wav
# game_06_09.sound.echo.echo_test()
game_06_09.sound.wav



class Grade:
    def __init__(self, score):
        self.score = score
    def __add__(self, other):
        result = self.score + other.score
        return result

math_score = Grade(50)
science_score = Grade(80)
print(math_score + science_score)





print(" ")
print(" ")