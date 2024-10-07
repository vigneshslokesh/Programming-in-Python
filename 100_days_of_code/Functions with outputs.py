
# this function returns the variable to where the function was called
def format_name(f_name,l_name):
    first = f_name.title()
    last = l_name.title()
    full_name = first +' '+last
    return full_name

formatted_string = format_name('vignesh','ReddY')
print(formatted_string)


# function to count the length in a text   
def length(param):
    count = 0
    for i in param:
        count += 1
    return count    
    
out = length("Vig")
print(out)