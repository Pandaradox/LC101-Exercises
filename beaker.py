
##################################################
#
#
# def course_grader(test_scores):
#     add_tests = 0
#     for test in test_scores:
#         if test <= 50:
#             print("fail1")
#         else:
#             add_tests += test
#             average = add_tests / len(test_scores)
#     print(average)
#     if average >= 70:
#         print("pass")
#     else:
#         print("fail2")
#
#
# def main():
#     test_scores = [80, 60, 60]
#     course_grader(test_scores)
#
#     print(course_grader([100, 75, 45]))     # "fail"
#     print(course_grader([100, 70, 85]))     # "pass"
#     print(course_grader([80, 60, 60]))      # "fail"
#     print(course_grader([80, 80, 90, 30, 80]))  # "fail"
#     print(course_grader([70, 70, 70, 70, 70]))  # "pass"
#
#
# if __name__ == "__main__":
#     main()

# ##################################################
#
#
# class Poop:
#     """Makes POOP?"""
#
#     def __init__(self, stink, color, corn):
#         self.stink = stink
#         self.color = color
#         self.corn = corn
#
#     def getstink(self):
#         return self.stink
#
#     def getcolor(self):
#         return self.color
#
#     def getcorn(self):
#         return self.corn
#
#     def status(self):
#         print("Gross! {color} poo stinks about {stink} out of 10!".format(
#         color = (self.getcolor()).upper(),
#         stink = self.getstink()))
#
# def main():
#     p = Poop(7, "brown", True)
#     print(p.getcorn())
#     p.status()
#
#
# if __name__ == "__main__":
#     main()

# ########################################
def boxBlur(image):
    final = []
    # for x in image:
    #     try:
    #         for y in image[x]:
    #             print(y)
    #             # final.append((
    #             #     image[x][y-1] +
    #             #     image[x][y+1] +
    #             #     image[x-1][y-1] +
    #             #     image[x-1][y] +
    #             #     image[x-1][y+1] +
    #             #     image[x+1][y-1] +
    #             #     image[x+1][y] +
    #             #     image[x+1][y+1])/8)
    #     except IndexError:
    #         continue
    final = []
    for x in range(1, len(image)-1):
        row = []
        for y in range(1, len(image[x])-1):
            row.append((
                image[x][y-1] +
                image[x][y] +
                image[x][y+1] +
                image[x-1][y-1] +
                image[x-1][y] +
                image[x-1][y+1] +
                image[x+1][y-1] +
                image[x+1][y] +
                image[x+1][y+1])//8)
        final.append(row)
    return(final)

def main():
    image = [(1,1,1,1,1),(1,2,7,2,1),(1,2,7,2,1),(1,1,1,1,1)]
    print(boxBlur(image))


if __name__ == "__main__":
    main()
