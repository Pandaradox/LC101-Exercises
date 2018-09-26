# ##################################################Exercise11-1: Char Count
# """This function takes a string of mixed upper and lowercase and returns
# the character count, ignoring spaces and non-alpha."""
#
#
# def charcount(line):
#     import string
#     line = line.lower()
#     alphainv = {}
#     for l in string.ascii_lowercase:
#         alphainv[l] = 0
#     for i in line:
#         if i in string.ascii_lowercase:
#             alphainv[i] += 1
#     return(alphainv)
#
#
# def main():
#     phrase = input("Please enter a phrase: ")  # "I like to move it move it. I like to move it move it.  I like to MOVE IT!"
#     results = charcount(phrase)
#     for i in results:
#         print(i, results.get(i, 0))
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise11-2&3: Grades
#
#
# def grades():
#     import os
#     roster = {}
#     name = "John"
#     while name.lower() != "q":
#         name = input("Enter student's name (q to quit): ")
#         if name.lower() == "q":
#             break
#         roster[name.capitalize()] = 0
#     avg = 0
#     for i, student in enumerate(roster, 1):
#         roster[student] = int(input("Grade for {}: ".format(student)))
#         avg += roster[student]
#     os.system("cls")
#     for n in roster:
#         print(n, roster[n])
#     return(avg / i)
#
#
# def main():
#     print("Average Grade:", str(grades())+"%")
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise11-4:


def main():

    print("Ham and Eggs")


if __name__ == "__main__":
    main()
