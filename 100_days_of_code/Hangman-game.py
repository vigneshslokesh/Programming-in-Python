import random
word_list = ["lorey","james","mermaid"]

rand_num = random.randint(0,2)
chosen_word = word_list[rand_num]
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)