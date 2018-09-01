# ##################################################Exercise 8-1: Triangle Numbers
# def trinum(t):
#     a = 0
#     next = 1
#     for i in range(t):
#         a += next
#         next += 1
#         print(a)
#
#
# def ask():
#     return(int(input("How many triangle numbers?")))
#
#
# def main():
#     try:
#         trinum(ask())
#     except ValueError:
#         print("Please enter a number...")
#         main()
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise 8-2: Turtle Dojo
#
#
# import turtle
# import random
#
#
# def training(dojo, t):
#     while t.xcor() < dojo.window_width()/2 \
#             and t.ycor() < dojo.window_height()/2 \
#             and t.xcor() > dojo.window_width()/-2 \
#             and t.ycor() > dojo.window_height()/-2:
#
#         turn(t)
#         # t.forward(random.randrange(1, 50))
#         t.forward(50)
#
#
# def turn(t):
#     coin = random.randrange(0, 1)
#     if coin == 1:
#         t.left(random.randrange(0, 180))
#     else:
#         t.right(random.randrange(0, 180))
#
#
# def main():
#
#     dojo = turtle.Screen()
#     don = turtle.Turtle()
#     don.color("purple")
#     don.speed(10)
#
#     training(dojo, don)
#     dojo.exitonclick()
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise 8-3: Two Turtle Dojo
#
#
# import turtle
# import random
#
#
# def training(dojo, t1, t2):
#     while (t1.xcor() < dojo.window_width()/2 \
#             and t1.ycor() < dojo.window_height()/2 \
#             and t1.xcor() > dojo.window_width()/-2 \
#             and t1.ycor() > dojo.window_height()/-2)\
#             and\
#             (t2.xcor() < dojo.window_width()/2 \
#             and t2.ycor() < dojo.window_height()/2 \
#             and t2.xcor() > dojo.window_width()/-2 \
#             and t2.ycor() > dojo.window_height()/-2)\
#             :
#
#         turn(t1)
#         t1.forward(50)
#         turn(t2)
#         t2.forward(50)
#
#
# def turn(spin):
#     coin = random.randrange(0, 1)
#     if coin == 1:
#         spin.left(random.randrange(0, 180))
#     else:
#         spin.right(random.randrange(0, 180))
#
#
# def main():
#
#     dojo = turtle.Screen()
#     don = turtle.Turtle()
#     don.color("purple")
#     don.speed(10)
#     mikey = turtle.Turtle()
#     mikey.color("orange")
#     mikey.speed(10)
#
#     training(dojo, don, mikey)
#     dojo.exitonclick()
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise 8-4: Turtle Battle
#
#
# import turtle
# import random
#
#
# def training(dojo, t1, t2):
#     splinter = 0
#     while (t1.xcor() <= dojo.window_width()/2
#             and t1.ycor() <= dojo.window_height()/2
#             and t1.xcor() >= dojo.window_width()/-2
#             and t1.ycor() >= dojo.window_height()/-2)\
#             and\
#           (t2.xcor() < dojo.window_width()/2
#             and t2.ycor() <= dojo.window_height()/2
#             and t2.xcor() >= dojo.window_width()/-2
#             and t2.ycor() >= dojo.window_height()/-2):
#
#         turn(t1)
#         moving(dojo, t1, t2)
#
#         turn(t2)
#         moving(dojo, t2, t1)
#         splinter += 1
#         if splinter == 30:
#             break
#
#
# def moving(dojo, f1, f2):
#     for i in range(0, 150):
#         clash(f1, f2)
#         parkour(dojo, f1)
#         f1.forward(1)
#
#
# def turn(spin):
#     coin = random.randrange(0, 1)
#     if coin == 1:
#         spin.left(random.randrange(91, 180))
#     else:
#         spin.right(random.randrange(91, 180))
#
#
# def parkour(dojo, b1):
#     if (b1.xcor() <= dojo.window_width()/-2
#             or b1.xcor() >= dojo.window_width()/2
#             or b1.ycor() <= dojo.window_height()/-2
#             or b1.ycor() >= dojo.window_height()/2):
#         b1.right(random.randrange(145, 180))
#         b1.write("Parkour!")
#         b1.forward(2)
#
#
# def clash(c1, c2):
#     if c1.xcor() == c2.xcor() and c1.ycor() == c2.ycor():
#         c1.right(180)
#         c1.forward(5)
#         c1.write("Hiyah!")
#         c2.left(180)
#         c2.forward(5)
#
#
# def main():
#
#     dojo = turtle.Screen()
#     dojo.tracer(25, 10)
#     dojo.screensize(100, 100)
#     don = turtle.Turtle()
#     don.color("purple")
#     don.speed(10)
#     don.goto(-50, 50)
#     mikey = turtle.Turtle()
#     mikey.color("orange")
#     mikey.speed(10)
#     mikey.goto(50, -50)
#
#     training(dojo, don, mikey)
#     dojo.exitonclick()
#
#
# if __name__ == "__main__":
#     main()
