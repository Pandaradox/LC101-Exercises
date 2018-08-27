# ##################################################
#
# def fart(x):
#     """This is a function for generating farts"""
#     for toots in range(x):
#         print("Toot")
#     if (x >= 10):
#         print("IMPRESSIVE!")
#
# x = int(input("How many beans did you eat? "))
# fart(x)
#
# print(fart.__doc__)
#

# ##################################################
#
# import turtle, random
# tess=turtle.Turtle()
# wn=turtle.Screen()
# rainbow = ["red", "orange", "yellow", "green", "blue", "violet"]
# tess.penup()
# tess.goto(-300,0)
# for sides in (3,4,6,8):
#    tess.penup()
#    tess.forward(100)
#    tess.pendown()
#    for i in range(sides):
#        tess.pencolor(random.choice(rainbow))
#        tess.forward(40)
#        tess.left(360/sides)
# wn.exitonclick()
# #################################################
# #################################################
# """Studio Fibbanaci Series"""
# def fib(x, y):
#     return y, x+y
#
# def main():
#     a = 0
#     b = 1
#     perms = int(input("Which sequence number do you want? "))
#     for i in range(perms-1):
#         print (a)
#         a, b = fib(a,b)
#     print(a, "Is the answer")
#
# if __name__ == "__main__":
#     main()
##################################################
##################################################
# import turtle
# import random
# tess=turtle.Turtle()
# wn=turtle.Screen()
# rainbow=["red","blue","yellow","orange","green","purple","hotpink"]
#
# tess.penup()
# tess.goto(-300,0)
# for sides in (3,4,6,8):
#    tess.penup()
#    tess.forward(100)
#    tess.pendown()
#    tess.color(random.choice(rainbow))
#    tess.begin_fill()
#    for i in range(sides):
#        tess.forward(40)
#        tess.left(360/sides)
#    tess.end_fill()
# wn.exitonclick()
##################################################
def square(num, iteration = 0, result = 0):
    num = abs(num)
    x = 1/1
    if iteration == num:
        return result
    return square(num, iteration+1, result + num)

def main():
    try:
        print("Square: ", square(10))
    except BaseException:
        print("Oopsie Daisy!")
    else:
        print("Error!")
if __name__ == "__main__":
    main()
