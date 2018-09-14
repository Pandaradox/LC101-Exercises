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
