from turtle import *
speed(0)

def em(size):
    width(3)
    left(90)
    forward(size)
    right(90+45)
    forward(size/2)
    left(90)
    forward(size/2)
    right(90+45)
    forward(size)

size = 100

for i in range(10):
    color("red")
    em(size)
    left(50)
    size+=2
    color("green")
    for j in range(50,70,5):
        em(j)
        left(23)
done()
