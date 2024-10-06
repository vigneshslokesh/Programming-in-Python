programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "An iterable, an action of doing something over and over again."
}

# Retrieve an item from the dictionary 
print(programming_dictionary['Bug'])

# adding name a new key value pair to the list
programming_dictionary["List"] = "A datastructure in python to store different elements"

# print all the elements in the dictionary
print(programming_dictionary)

# creating a new empty dictionary
empty_dict = {}

#  edit an item in a dictionary
programming_dictionary['Bug'] = 'An error which doesn\'t allow a program to run.'
print(programming_dictionary["Bug"])

# Loop through a dictionary
for obj in programming_dictionary:
    print(obj)
    print(programming_dictionary[obj])