from art import logo, vs
from game_data import data
import random

random_gen = random.choice(data)

def formattable(account):
    account_name = account["name"]
    account_count = account["follower_count"]
    account_desc = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b "
    
    pass

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {formattable(account_a)}")
print(f"Compare B: {formattable(account_b)}")

guess = input("Who has more followes? Type 'A' or 'B': ").lower()

a_follower_count = account_a["follower_count"]
b_followe_count = account_b["follower_count"]

is_correct = check_answer(guess,a_follower_count,b_followe_count)