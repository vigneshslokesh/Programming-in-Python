def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

opt = {"+": add, "-": sub, "*": mul, "/": div}

# print(opt["*"](2,2))

n1 = float(input("Enter the first number: "))
for i in opt:
    print(i)
option = input("Enter the mathematical operator: ")
n2 = float(input("Enter the second number: "))

print(opt[option](n1,n2))

# for i in opt:
#     if option in i:
#         func = opt[i]

# res = func(n1,n2)
# print(f"The answer is {res}.")