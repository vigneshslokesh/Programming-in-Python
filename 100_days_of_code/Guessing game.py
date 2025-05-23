import random


def predictor(attempts):
    while attempts>0:
        print(f"You have {attempts} attempts left to guess a number.")
        # print(f"Computer number is {the_num}")
        guess = int(input("Make a guess: "))
        if guess == the_num:
            print(f"Your guess is correct: {guess}")
            break
        elif guess!= the_num:          
            if guess < the_num:
                print("Too low.")
            elif guess > the_num:
                print("Too high")
            attempts -= 1
            
            if attempts>0:
                print("Guess again")
            
    if attempts ==0:
        print("You loose, out of attempts!")
    else:
        print("You Win!!")



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
the_num = random.randint(1,100)

difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 5
    predictor(attempts)
else:
    attempts = 10
    predictor(attempts)