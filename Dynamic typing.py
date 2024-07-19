#We are trying to illustrate what we call the dynamic typing

a=10
print(type(a))

a='India'
print(type(a))

n=10
print(type(n))
print(n)
n=n/2
#when we use (/) division it converts it into float 
print(type(n))
print(n)

#shorthand operators
#in operator
#chaining expression

x = 5
print(1<x<10)
print(10<x<20)
print(x<10<x*10<100)
print(10>x<=9)
print(5==x >4)