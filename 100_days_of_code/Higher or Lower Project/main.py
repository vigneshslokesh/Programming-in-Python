from art import logo, vs
from game_data import data
import random

random_gen = random.choice(data)

def formattable(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_count = account["follower_count"]
    account_desc = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b "
    

game_cont = True

# Generate a random account from the game data
# account_a = random.choice(data)
account_b = random.choice(data)
score = 0
print(logo)

while game_cont:
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formattable(account_a)}")
    print(vs)
    print(f"Compare B: {formattable(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followes? Type 'A' or 'B': ").lower()

    # clear the screen
    print("\n"*20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_followe_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_followe_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_cont = False