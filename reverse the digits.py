def reversefunction(num):
    rev_num = 0

    while(num>0):
        rev_num = rev_num * 10 + num % 10 
        # extract the last digit and update the rev_num

        num = num // 10
        # remove the last digit from num

    return rev_num

number = int(input("Enter a number: "))
reversed_num = reversefunction(number)
print(reversed_num)