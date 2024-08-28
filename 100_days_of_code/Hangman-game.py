import random
word_list = ["lorey","james","mermaid"]

# rand_num = random.randint(0,2)
# chosen_word = word_list[rand_num]

#random
#randint
#choice
#shuffle

chosen_word = random.choice(word_list) # more line saving and efficient
print(chosen_word) 

guess = input("Guess a letter: ").lower()
if guess in chosen_word:
    print('Correct')
else:
    print('Wrong')