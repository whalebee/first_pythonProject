import inspect
import random

print(inspect.getfile(random)) # 파일의 경로가 나옴
print(inspect.getsource(random.randint)) # return self.randrange(a, b+1)
print(inspect.getsource(random.randrange)) # 오 많다

property