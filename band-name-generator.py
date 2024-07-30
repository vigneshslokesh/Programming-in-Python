print("When did India get its independence (year)?")
year = int(input())

if (year==1947):
    print("Great! you are correct.")

else:
    print("Comeon dont you know this?")
    print("Thats okay, I will give you a second chance.")
    year = int(input())
    if(year==1947):
        print("You got it right!")
    else:
        print("Failed in second attempt too?")