from game_data import data
import random

# print(data[0])
def random_gen():
    return random.choice(data)

comp_a = random_gen()
comp_b = random_gen()

while comp_b == comp_a:
    comp_b = random_gen()

# print(comp_a)
# print(comp_b)

score = 0

def compare(choice, comp_a, comp_b):
    if comp_a['follower_count'] > comp_b['follower_count']:
        ans = 'a'
        # comp_b = random_gen()
    else:
        ans = 'b'
        # comp_a = comp_b
        # comp_b = random_gen()
    return choice == ans


    
print(comp_a)
print(comp_b)


while True:
    print(f"Compare A: {comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}")
    print(f"Compare B: {comp_b['name']}, a {comp_b['description']}, from {comp_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if compare(choice, comp_a, comp_b):
        score += 1
        print(f'Correct! Your score: {score}')
        comp_a = comp_b
        comp_b = random_gen()
    else:
        print(f"Wrong answer, your score: {score}")
        break
