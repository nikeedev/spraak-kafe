from funcs import *

def say(inputt): 
    print(inputt)



t.showturtle()

print("FUS - Språk Kafe! - Bruno Leite. Bygget av Nikita @2022")

print(sc.screensize())

t.penup()

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
say("Arm1 pos: ")
say(t.pos())
pos1 = t.pos()
say("\n")

t.seth(0)
t.left(90)
t.circle(120, 90)

#t.forward(110)

# klippen: 

t.forward(31.36)
t.seth(225)
t.forward(27.5)
t.seth(135)
t.forward(27.5)
say("Klipp pos: ")
say(t.pos())
#t.seth(0)
say("\n")
t.seth(180)
t.forward(27.5)

say(t.pos())


###############################################


# Andre side: 
# """
t.penup()
t.seth(0)
t.setposition(-130, -280)
print(t.pos())
t.seth(89)
t.pendown()

# Arm2

t.forward(272)


# T-skjorte_Arm.2

t.left(90)
t.forward(45)

say("Arm2 pos: ")
say(t.pos())
pos2 = t.pos()
say("\n")

t.seth(0)
t.right(90)
t.circle(120, -90)
t.seth(0)
t.forward(28)

# Tegne armene 

# Ekte arm.1
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
t.penup()

say("Heading: ")
say(t.heading())

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

#"""
say(t.pos())

t.hideturtle()

sc.exitonclick()

exit(0)
