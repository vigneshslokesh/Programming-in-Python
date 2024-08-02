choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
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
print("Your choice")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

import random
print("Computer choice")
computer = random.randint(0,2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if choice == computer:
    print("It's a draw")
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
else:
    print("You win")