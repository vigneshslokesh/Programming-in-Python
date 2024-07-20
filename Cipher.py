alpha = 'abcdefghijklmnopqrstuvwxyz'

i = 25

# mod of the next index out of range gives the 
# first character of the string
# making sure it does not go out of bound

print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])

x = 'india'
# I expect to output joejb

y=''