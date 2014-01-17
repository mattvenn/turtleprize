from turtle import *

fillcolor("yellow")
shape("square")
loops = 0

while loops < 60:
    stamp()
    forward(30)
    #turn left a little bit more each time
    left(loops)
    #increment loop counter
    loops = loops + 1

done()
