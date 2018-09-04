
##################################################


def course_grader(test_scores):
   add_tests = 0
   for test in test_scores:
       if test <= 50:
           print("fail1")
       else:
           add_tests += test
           average = add_tests / len(test_scores)
   print(average)
   if average >= 70:
       print("pass")
   else:
       print("fail2")

def main():
   test_scores = [80,60,60]
   course_grader(test_scores)
   print(print("Hello"))



   print(course_grader([100,75,45]))     # "fail"
   print(course_grader([100,70,85]))     # "pass"
   print(course_grader([80,60,60]))      # "fail"
   print(course_grader([80,80,90,30,80]))  # "fail"
   print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
   main()
