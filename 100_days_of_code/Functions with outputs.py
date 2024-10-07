
# # this function returns the variable to where the function was called
# def format_name(f_name,l_name):
#     first = f_name.title()
#     last = l_name.title()
#     full_name = first +' '+last
#     return full_name

# formatted_string = format_name('vignesh','ReddY')
# print(formatted_string)


# # function to count the length in a text   
# def length(param):
#     count = 0
#     for i in param:
#         count += 1
#     return count    
    
# out = length("Vig")
# print(out)

# function with multiple return
def full_name(f_name,l_name):
    """"Docstrings"""
    if f_name =='' and l_name == '':
        return ("Enter a valid name!")
    first = f_name.title()
    last = l_name.title()
    return (f"{first} {last}")

name = full_name(input("Enter your first name: "),input("Enter your last name: "))
print(name)