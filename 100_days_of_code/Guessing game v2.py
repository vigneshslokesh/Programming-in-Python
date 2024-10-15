import random

EASY_LEVEL = 10 ###
HARD_LEVEL = 5

# Function to check users' guess against actual answer
def check_answer(guess, the_num, turns):
    if guess < the_num:
        print("Too low.")
        return turns-1 ###
        
    elif guess > the_num:
        print("Too high")
        return turns-1 ###
        
    else:
        print(f"You got it! The answer was {the_num}")
        return -1      
            
# Function to set difficulty            
def set_difficulty():
    difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL       
    else:
        return HARD_LEVEL
        

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    # Choosing a random number between 1 and 100.
    the_num = random.randint(1,100)
    print(f"Computer number is {the_num}")
    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess!=the_num:
        print(f"You have {turns} attempts left to guess a number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, the_num, turns) ###
        if turns>0:
            print("Guess again")
        if turns ==0:
            print("You loose, out of attempts!")
            break

game()

