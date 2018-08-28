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
# ##################################################
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
#
#
# def square(num, iteration=0, result=0):
#     num = abs(num)
#     if iteration == num:
#         return result
#     return square(num, iteration+1, result + num)
#
#
# def main():
#     print("Square: ", square(10))
#
#
# if __name__ == "__main__":
#     main()
# ##################################################
##################################################
# Testing errors
#
#
# def oops(s):
#     # print(poop)
#     print(int(u'\u0394'))
#
#
# def main():
#
#     x = 0
#     try:
#         oops(x)
#     except ValueError:
#         print("oops")
#
#
# if __name__ == "__main__":
#     main()
##################################################
#
#
# def main():
#
#     table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
#     for name, phone in table.items():
#         print(f'{name:10} ==> {phone:10d}')
#
#
# if __name__ == "__main__":
#     main()
#
##################################################
##################################################


def main():

    print("Ham and Eggs")


if __name__ == "__main__":
    main()
