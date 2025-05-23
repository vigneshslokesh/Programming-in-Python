print("When did India get its independence (year)?")
year = int(input())

# if (year==1947):
#     print("Great! you are correct.")

# else:
#     print("Comeon dont you know this?")
#     print("Thats okay, I will give you a second chance.")
#     year = int(input())
#     if(year==1947):
#         print("You got it right!")
#     else:
#         print("Failed in second attempt too?")

#I would like to write a piece of code which lets the user as many times he wants.
#The code will end, only when the user gets it right.

while(year!=1947): #until this statement/condition becomes false
    print("You got this wrong, Enter once again.")
    year = int(input())

print("Wow! you got it right.")

# while works like this
    # while <condition>
        # write whatever you want here
        # write whatever you want here

    # loop exits when the condition is wrong. runs until the condition becomes false