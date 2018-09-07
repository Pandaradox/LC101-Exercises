# ##################################################Exercise 9-1:Str Statements
#
#
# def main():
#
#     print(
#     "Python"[1],
#     "Strings are sequences of characters."[5],
#     len("wonderful"),
#     "Mystery"[:4],
#     "p" in "Pineapple",
#     "apple" in "Pineapple",
#     "pear" not in "Pineapple",
#     "apple" > "pineapple",
#     "pineapple" < "Peach")
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise 9-2:Integer Digits
#
#
# def digitsin(x):
#     return(len(str(x)))
#
# def main():
#
#     print(digitsin(1000))
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise 9-3:String Surgery
#
#
# def remove(substr, ogstr):
#
#     if substr in ogstr:
#         return(
#             ogstr[:ogstr.find(substr)]
#             + ogstr[ogstr.find(substr) + len(substr):])
#     else:
#         return(ogstr)
#
#
# def main():
#     print(remove('an', 'banana'))
#     print(remove('cyc', 'bicycle'))
#     print(remove('iss', 'Mississippi'))
#     print(remove('egg', 'bicycle'))
#     print(remove('oo', 'Yahoohoo'))
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise 9-4:Reverse String
#
#
# def flop(flip):
#     newstr = ""
#     for i in range(len(flip)-1, -1, -1):
#         newstr += flip[i]
#     return(newstr)
#
# def main():
#
#     print(flop("Ham and Eggs"))
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Studio: Bubble Sort


def bubble_sort(bubble):
    if len(bubble) == 1:
        return(bubble)
    x = 0
    while x == 0:
        for i in range(len(bubble)-1):
            if bubble[i] > bubble[i+1]:
                y = bubble[i]
                bubble[i] = bubble[i+1]
                bubble[i+1] = y
        for i in range(len(bubble)-1):
            if bubble[i] > bubble[i+1]:
                x == 0
                break
            else:
                x = 1
    return(bubble)


def main():

    print(bubble_sort([0]), [0])
    print(bubble_sort([1, 2, 3, 4, 5, 3, 5, 6, 7]), [1, 2, 3, 4, 5])
    print(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    print(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()
