stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

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

# for i in chosen_word:
#     print('_', end='')

place_holder = ""
for pos in range(len(chosen_word)):
    place_holder += '_'

print(place_holder)

correctletter = []
gameover = False
lives = 6

while not gameover: 
    guess = input("Guess a letter: ").lower()
    # print(guess)


    display = ""


    for letter in chosen_word:  #confusing!!!!
        if letter == guess:
            display += letter
            correctletter.append(guess)
        elif letter in correctletter:
            display += letter
        else:
            display += '_'

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            gameover = True 
            print("You lose!")

    print(display)

    if '_' not in display:
        gameover = True
        print('You win!')