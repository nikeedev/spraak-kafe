import time
from funcs import *


def say_skjer(inputt):
    print("Skjer nå: " + str(inputt))


def say(inputt):
    print(str(inputt))


t.showturtle()

print("FUS - 10. trinn - Språk Kafe! - Bruno Leite. Bygd av Nikita @ 2022")

print(sc.screensize())

say_skjer("\nStart:\n")

#while True:
t.penup()

# Hode

t.setpos(36.89, 112.74)
t.pendown()


t.color("black", "#d8854c")
t.begin_fill()

# hals 1  

t.seth(88)
t.forward(40)

t.seth(75)
t.circle(100, 20)


# Totalt forward: 46 pixels
say("denne:")
say(t.pos())
say("\n")
t.forward(11.5)
t.seth(25)


t.circle(15, 110)
t.seth(180)
t.forward(4.95)
say("høyre øyre pos: ")
say(t.pos())
say("\n")
t.seth(90)
t.backward(34.5)
t.forward(44.5) # +10 px

t.circle(50, 180)

t.forward(10)

# venstre øyre

t.forward(34.5) # +10 px
t.backward(34.5)
say("Venstre øyre pos: ")
say(t.pos())
say("\n")
t.seth(180)
t.forward(4.95)
t.seth(-135)
t.circle(15, 110)
t.seth(180)


# time.sleep(2)

# t.penup()

# Hals 2

# t.setpos(-44.89, 112.74)
# t.pendown()


t.seth(268)

t.circle(100, 25)
say_skjer(f"Munn pos: {t.pos()}")

t.seth(272)
t.forward(43.51)


say("Klipp pos hals: "+ str(t.pos()))
say("\n")

say_skjer("\nklippen:\n")
t.seth(0)
t.forward(31.36)
say("\netter Klipp pos:")
say(t.pos())
say("\n")
t.seth(-45)
t.forward(27.5)
say("\nKlipp pos:")
say(t.pos())
say("\n")
t.seth(45)
t.forward(27.5)
say("\nfør Klipp pos:")
say(t.pos())
say("\n")
t.seth(0)
t.forward(18)
t.seth(90)
t.forward(5)

t.penup()
t.end_fill()

# TODO: Create eyes.


# Høyre øye

t.setpos(39.63, 202.97)
t.seth(180)
t.forward(16.5)
t.seth(90)

t.color("black", "white")
t.begin_fill()
t.pendown()
t.circle(10, 175)
t.seth(0)
t.forward(20)
t.end_fill()
t.penup()

t.color("black", "black")
t.backward(10)
t.seth(90)
t.forward(4)
t.pendown()
t.begin_fill()
t.circle(1.75)
t.end_fill()
t.penup()


t.seth(180)
t.backward(12)
t.forward(6)
t.seth(90)
t.forward(10)

t.pendown()

t.seth(115)

t.circle(10, 145)

t.penup()

################

# Venstre øye

t.seth(0)
t.setpos(-60.37, 202.97)
t.forward(16.5*2)
t.seth(90)

t.color("black", "white")
t.begin_fill()
t.pendown()
t.circle(10, 175)
t.seth(0)
t.forward(20)
t.end_fill()
t.penup()

t.color("black", "black")
t.backward(7)
t.seth(90)
t.forward(4)
t.pendown()
t.begin_fill()
t.circle(1.75)
t.end_fill()
t.penup()


t.seth(0)
t.backward(-2)
t.forward(6)
t.seth(90)
t.forward(10)

t.pendown()

t.seth(115)

t.circle(10, 145)

print(t.pos())

t.end_fill()
t.penup()

t.home()

t.setpos(-20, 161)

#time.sleep(5)

#t.clear()

"""

########### # # # #############################
##### # # # # ############ T-skjorte
############ # # # ############################

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
#t.hideturtle()

sc.exitonclick()  

exit(0)
