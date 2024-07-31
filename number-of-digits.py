num = abs(int(input("Enter a number: ")))
#input from user -> convert to int -> absolute value
#abs - ignore the sign of a number

digit = 1
while(num > 9):
    num = num // 10 # reduce the number 
    digit = digit + 1

print(digit)

