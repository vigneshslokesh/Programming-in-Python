# Let us find the factorial of a number

# print("Enter a number")
# n = int(input())

#n = 5
#factorial of n is 1*2*3*4*5

# i = 1
# answer = 1
# while(i<=n): # less than or equal to - cannot be greater than n
#     answer= answer*i
#     i=i+1

# print(answer)

#i keeps in incrementing
#CTRL + C -> exit code

# <-------->
#alternative
num = int(input("Enter a number"))
fact = 1

while(num>0):
    fact = fact * num
    num = num-1

print(fact)