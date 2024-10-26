from art import logo, vs
from game_data import data
import random

random_gen = random.choice(data)

def formattable(account):
    account_name = account["name"]
    account_count = account["follower_count"]
    account_desc = account["decription"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc}, from {account_country}"


account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {formattable(account_a)}")
print(f"Compare B: {formattable(account_b)}")