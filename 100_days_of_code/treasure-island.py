print('''  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossover = input("You are in a crossover, Do you wanna go 'left' or 'right'?").lower()
if(crossover == "left"):
    choice = input("There is a lake which has a island in centre, do you wanna 'swim' or 'wait' foor the boat?").lower()
    if(choice == "wait"):
        door = input("You reached safely. There is a blue door, red door, yellow door, which one do you wanna open?").lower()
        if door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        else: 
            print("You chose a door that does not exist, Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")