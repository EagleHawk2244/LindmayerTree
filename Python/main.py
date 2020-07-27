import turtle
import time
t = turtle.Pen()

branch = []
code = "1[0]0" # Change this to modify the structure of the tree

t.left(90)
t.up()
t.backward(300)
t.down()
t.speed(10)


for c in code:
    if c == "1":
        t.pencolor("brown")
        t.forward(100) # Change this to modify the size of the tree

    elif c == "0":
        t.pencolor("green")
        t.forward(3) # Change this to modify the size of the leaves

    elif c == "[":
        t.left(45)
        branch.append((t.position(), t.heading()))

    elif c == "]":
        t.up()
        t.goto(branch[len(branch) -1][0], None)
        t.setheading(branch[len(branch) -1][1])
        t.right(90)
        t.down()
        del branch[len(branch) -1]
