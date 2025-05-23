print("Its\'s a beautiful day")
# \ - backslash are used to escape a charcter in front of it

print("We are from 'BIT' Bangalore")

print("My name is Octa.\n\tI am from Bangalore")
#\t - escape character called tab
#\n - escape character called new line

x = 'This is a string'
y = 'This is also a string'
z = '''first line
second line
third line'''
#statements exceeding more than single line are quoted under three quotes

print(x)
print(y)
print(z)

#methods in python
# m = 'pytHoN sTrIng mEthOdS'
# print(m.lower())
# print(m.upper())
# print(m.capitalize())
# print(m.title())
# print(m.swapcase())

# n = 'Python'
# print(n.islower())
# print(n.isupper())
# print(n.istitle())

m = '123'
print(m.isdigit())

m = 'abc'
print(m.isalpha())

m= 'abs123'
print(m.isalnum())

x = '------Python--abc-----'
print(x.strip('-'))

print(x.lstrip('-'))

print(x.rstrip('-'))

y = 'Python'
print(y.startswith('P'))
print(y.startswith('p'))
print(y.endswith('n'))
print(y.endswith('N'))

z = 'Python String Methods'
print(z.count('t'))
print(z.count('s'))

print(z.index('t'))
print(z.index('s'))

z = z.replace('S','s')
z = z.replace('M','m')
print(z)