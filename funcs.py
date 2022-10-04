import turtle

t = turtle.Turtle()
sc = turtle.Screen()

t.speed(6)


def femkant(moves_px, degrees):
    for _ in range(6):
        print(t.pos())
        t.forward(moves_px)
        print(t.pos())
        t.left(degrees)

