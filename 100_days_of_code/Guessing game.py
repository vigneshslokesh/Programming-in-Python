import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
the_num = random.randint(1,100)

difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 5
    while attempts==0:
        print(f"You have {attempts} attempts left to guess a number.")
        guess = int(input("Make a guess: "))
        if guess == the_num:
            print(f"Your guess is correct: {guess}")
        elif guess!= the_num:
            
            if guess < the_num:
                print("Too low.")
            elif guess > the_num:
                print("Too high")
            print("Guess again")
            attempts -= 1
    
    
# else:
#     attempts = 3
#     pass
