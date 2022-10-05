from funcs import *

t.showturtle()

print("Språk Kafe - FUS!")

print(sc.screensize()[0])

t.penup()

t.seth(90)
t.setposition(130, -280)
print(t.pos())
t.seth(91)
t.pendown()

t.forward(272)
t.right(90)
t.forward(45)
t.left(90)

print(t.pos())

# ferdig
# t.hideturtle()
sc.exitonclick()
