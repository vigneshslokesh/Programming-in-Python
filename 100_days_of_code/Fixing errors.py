# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("You have typed a invalid number, try with numberical number")
#     age = int(input("Enter your age: "))

# if age>=18:
#     print(f"You can drive at age {age}.")
# else:
#     print(f"You can't drive at age {age}")


# print() statements to fix errors

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)