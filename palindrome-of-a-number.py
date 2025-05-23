def palindrome(num):
    org_num = num
    rev_num = 0

    while(num>0):
        rev_num = rev_num * 10 + num % 10 
        # extract the last digit and update the rev_num

        num = num // 10
        # remove the last digit from num

    return org_num == rev_num

number = int(input("Enter a number: "))
if palindrome(number):
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")