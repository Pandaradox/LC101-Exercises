import turtle

def mini_square(t, size = 50):
    for i in range(4):
        t.forward(size)
        t.left(90)

def biggy_square(t,size = 50):
    for i in range(4):
        mini_square(t, size)
        t.left(90)

def main():
    canvas = turtle.Screen()
    canvas.bgcolor("light green")
    zeke = turtle.Turtle()
    zeke.pensize(3)
    zeke.pencolor("blue")
    zeke.speed(0)
    num_of_squares = 10
    square_size = 200
    for squares in range(num_of_squares):
        biggy_square(zeke, square_size)
        zeke.left(90/num_of_squares)
    canvas.exitonclick()
if __name__ == "__main__":
    main()
