from math import sqrt
from turtle import fd, rt, done, circle

PHI = 1 / ((sqrt(5) - 1) / 2)

print(PHI)

# def square(n: int):
#     for _ in range(4):
#         fd(n)
#         rt(89)

def spiral(times: int) -> None:
    length = 5
    for _ in range(times):
        circle(length, 90)
        length *= PHI


        
if __name__ == '__main__':
    # for _ in range(300):
    #     square(100)
    #     rt(60)
    
    spiral(20)
    done()