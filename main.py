import time
from funcs import *


def say_skjer(inputt):
    print("Skjer nå: " + str(inputt))


def say(inputt):
    print(str(inputt))


t.showturtle()

print("FUS - Språk Kafe! - Bruno Leite. Bygget av Nikita @2022")

print(sc.screensize())



say_skjer("\nStart:\n")

t.penup()

# Hode

t.setpos(36.89,112.74)
t.pendown()

t.seth(92)
t.forward(40)

t.seth(75)
t.circle(100, 20)

# Totalt forward: 46 pixels 
t.forward(11.5)
say("høyre øyre pos: ")

say(t.pos())
time.sleep(2)

t.penup()
"""
# T-skjorte

t.seth(90)
t.setposition(130, -280)
print(t.pos())
t.seth(91)
t.pendown()
t.forward(272)

# Arm1

t.right(90)
t.forward(45)

# T-skjorte_Arm.1
say_skjer("\nT-skjorte_Arm.1:\n")
say_skjer("Arm1 pos: ")
say_skjer(t.pos())
pos1 = t.pos()
say_skjer("\n")

t.seth(0)
t.left(90)
t.circle(120, 90)

# t.forward(110)

# klippen: 
say_skjer("\nklippen:\n")
t.forward(31.36)
say("\nfør Klipp pos:")
say(t.pos())
say("\n")
t.seth(225)
t.forward(27.5)
say("\nKlipp pos:")
say(t.pos())
say("\n")
t.seth(135)
t.forward(27.5)
say("\netter Klipp pos:")
say(t.pos())
say("\n")
# t.seth(0)
t.seth(180)
t.forward(27.5)

say_skjer(t.pos())

###############################################


# Andre side: 
"""
"""
say_skjer("\nAndre side:\n")

t.penup()
t.seth(0)
t.setposition(-130, -280)
print(t.pos())
t.seth(89)
t.pendown()

# Arm2

say_skjer("\nArm2:\n")

t.forward(272)

# T-skjorte_Arm.2

say_skjer("\nT-skjorte_Arm.2:\n")

t.left(90)
t.forward(45)

say_skjer("\nArm2 pos:\n")
say_skjer(t.pos())
pos2 = t.pos()
say_skjer("\n")

t.seth(0)
t.right(90)
t.circle(120, -90)
t.seth(0)
t.forward(28)

# Tegner armene 

say_skjer("\nTegner armene:\n")

# Ekte arm.1

say_skjer("\nEkte arm.1:\n")

t.penup()

t.setpos(pos1)
t.pendown()
t.color("black", "#d8854c")
t.begin_fill()

t.seth(-95)
t.forward(40)
t.seth(-106)
t.forward(140)
t.seth(91)
t.forward(174.39)
t.seth(0)
t.forward(45)
t.end_fill()

# Ekte arm.2

say_skjer("\nEkte arm.2:\n")

t.penup()

say_skjer("Heading: ")
say_skjer(t.heading())

t.setpos(pos2)
t.pendown()
t.color("black", "#d8854c")
t.begin_fill()

t.seth(275)
t.forward(40)
t.seth(286)
t.forward(140)
t.seth(89)
t.forward(174.39)
t.seth(180)
t.forward(45)
t.end_fill()

# ferdig
t.penup()

t.home()
t.seth(90)


# say_skjer(t.pos())
"""
t.hideturtle()

sc.exitonclick()

exit(0)
