from funcs import *

t.showturtle()

print("Språk Kafe - FUS!")

t.color("black")
t.begin_fill()

print(t.pos())
femkant(50, 72)
t.end_fill()
femkant(50, -72)
t.setposition(20, -100)
t.circle(120)

# t.hideturtle()
sc.exitonclick()
