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


def claculator():
    n1 = float(input("Enter the first number: "))

    accumulate = True
    while accumulate:
        
        for i in opt:
            print(i)
        option = input("Enter the mathematical operator: ")
        n2 = float(input("Enter the second number: "))

        ans = opt[option](n1,n2)
        print(f"{n1} {option} {n2} = {ans}")
        cont = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ").lower()

        if cont == 'y':
            n1 = ans
        
        else: 
            accumulate = False
            print("\n" * 10)
            claculator()
    
claculator()









# for i in opt:
#     if option in i:
#         func = opt[i]

# res = func(n1,n2)
# print(f"The answer is {res}.")