print("Welcome to Rollercoaster ticket vending machine")
height = int(input("Enter your height in cm: "))
bill = 0
if(height>120):
    print("You can ride the Rollercoaster")
    age = int(input("Enter your age: "))
    if(age < 12):
        print("Child ticket price is $5.")
        bill += 5
    elif(age <= 18):
        print("Youth ticket price is $7.")
        bill += 7
    elif(age>= 45 and age<= 55):
        print("Everythong will be okay!, the ticket is on us.")
    else:
        print("Adult ticket price is $12")
        bill += 12
    
    wants_a_photo = input("Do you want a photo taken? Y or N. ")
    if wants_a_photo == "Y":
        print("Photo charges is $3.")
        bill += 3

    print(f"The final bill is ${bill}.")

else:
    print("Sorry, you don't have enough height to ride the Rollercoaster.")