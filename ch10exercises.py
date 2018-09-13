# ##################################################Exercise10-2
#
# """Build a list containing 76, 92.3, "hello", True, 4, 76 using concatenation,
#     and append methods"""
#
#
# def main():
#
#     mylistcon = [76]
#     mylistcon += [92.3]
#     mylistcon += ["hello"]
#     mylistcon += [True]
#     mylistcon += [4]
#     mylistcon = mylistcon + [76]
#     print("mylist concatenated: ", mylistcon)
#
#     mylistapp = []
#     mylistapp.append(76)
#     mylistapp.append(92.3)
#     mylistapp.append("hello")
#     mylistapp.append(True)
#     mylistapp.append(4)
#     mylistapp.append(76)
#     print("mylist appended: ", mylistapp)
#
#
# if __name__ == "__main__":
#     main()
#
#

# ##################################################Exercise10-3: List Manip
#
# """
# Append “apple” and 76 to the list.
# Insert the value “cat” at position 3.
# Insert the value 99 at the start of the list.
# Find the index of “hello”.
# Count the number of 76s in the list.
# Remove the first occurrence of 76 from the list.
# Remove True from the list using pop and index."""
#
#
# def main():
#
#     mylist = [76, 92.3, "hello", True, 4, 76]
#     print("1. ", mylist)
#     mylist.append("apple")
#     mylist.append(76)
#     print("2. ", mylist)
#     mylist.insert(3, "cat")
#     print("3. ", mylist)
#     mylist.insert(0, 99)
#     print("4. ", mylist)
#     print("5. Index of 'hello': ", mylist.index("hello"))
#     print("6. The number of 76s in the list: ", mylist.count(76))
#     mylist.remove(76)
#     print("7. ", mylist)
#     mylist.pop(4)
#     print("8. Pop: ", mylist)
#     mylist.insert(4, True)
#     print("8. Index'd: ", mylist)
#     mylist.pop(mylist.index(True))
#     print("8. Index'd: ", mylist)
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise10-4: Odd Numbers
#
#
# def oddcount(num):
#     count = 0
#     results = []
#     for i in num:
#         if num[i] % 2 != 0:
#             count += 1
#             results.append(num[i])
#     return(count, results)
#
#
# def main():
#     numbers = range(26)
#     count, results = oddcount(numbers)
#     print(count, "odd numbers:")
#     print(results)
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Exercise10-5: Max Number
# import random
#
#
# def max(num):
#     king = 0
#     for i in num:
#         if i > king:
#             king = i
#     return(king)
#
#
# def main():
#     numbers = (random.sample(range(1000), k=100))
#     print(numbers)
#     print(max(numbers))
#
#
# if __name__ == "__main__":
#     main()

# ##################################################Studio: Bubble Sort
#
#
# def bubble_sort(bubble):
#     if len(bubble) == 1:
#         return(bubble)
#     x = 0
#     while x == 0:
#         for i in range(len(bubble)-1):
#             if bubble[i] > bubble[i+1]:
#                 y = bubble[i]
#                 bubble[i] = bubble[i+1]
#                 bubble[i+1] = y
#         for i in range(len(bubble)-1):
#             if bubble[i] > bubble[i+1]:
#                 x == 0
#                 break
#             else:
#                 x = 1
#     return(bubble)
#
#
# def main():
#
#     print(bubble_sort([0]), [0])
#     print(bubble_sort([1, 2, 3, 4, 5, 3, 5, 6, 7]), [1, 2, 3, 4, 5])
#     print(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
#     print(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
#
#
# if __name__ == "__main__":
#     main()
