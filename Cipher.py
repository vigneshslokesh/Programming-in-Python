alpha = 'abcdefghijklmnopqrstuvwxyz'

# i = 25

# mod of the next index out of range gives the 
# first character of the string
# making sure it does not go out of bound

# print(alpha[i%26])
# print(alpha[(i+1)%26])
# print(alpha[(i+2)%26])

x = 'india'
# I expect to output joejb

# encrypting with k as the key
y=''
i=0
k=20
y=y+(alpha[(((alpha.index(x[i]))+k)%26)])
y=y+(alpha[(((alpha.index(x[i+1]))+k)%26)])
y=y+(alpha[(((alpha.index(x[i+2]))+k)%26)])
y=y+(alpha[(((alpha.index(x[i+3]))+k)%26)])
y=y+(alpha[(((alpha.index(x[i+4]))+k)%26)])

print(y)

# decrypting with k as the key

z=''
z=z+(alpha[(((alpha.index(y[i]))-k)%26)])
z=z+(alpha[(((alpha.index(y[i+1]))-k)%26)])
z=z+(alpha[(((alpha.index(y[i+2]))-k)%26)])
z=z+(alpha[(((alpha.index(y[i+3]))-k)%26)])
z=z+(alpha[(((alpha.index(y[i+4]))-k)%26)])

print(z)
