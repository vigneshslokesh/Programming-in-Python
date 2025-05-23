
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice >= 3 or choice < 0:
    print("Invalid choice, you lose!")
    exit
else:
    print("Your choice")
    print(game_images[choice])

    import random
    print("Computer choice")
    computer = random.randint(0,2)
    print(game_images[computer])

    if choice == computer:
        print("It's a draw")
    elif choice>= 3 or choice < 0:
        print("Invalid choice")
    elif choice == 0 and computer == 1:
        print("You lose")
    elif choice == 0 and computer == 2:
        print("You win")
    elif choice == 1 and computer == 0:
        print("You win")
    elif choice == 1 and computer == 2:
        print("You lose")
    elif choice == 2 and computer == 0:
        print("You lose")
    elif choice == 2 and computer == 1:
        print("You win")