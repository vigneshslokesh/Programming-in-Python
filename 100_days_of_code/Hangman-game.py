

import random

from hangman_words import word_list
from hangman_art import stages
# rand_num = random.randint(0,2)
# chosen_word = word_list[rand_num]

#random
#randint
#choice
#shuffle
# print(logo)


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

    print(f"****************** {lives} / 6 LIVES LEFT")
    guess = input("Guess a letter: ").lower()
    # print(guess)

    if guess in correctletter:
        print(f'You have already guessed the {guess}')

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
        print(f"You guessed {guess}, that's not in the word. You loose a life")
        if lives == 0:
            gameover = True 
            print(f"******************You lose! it was {chosen_word}******************")

    print(display)

    if '_' not in display:
        gameover = True
        print('******************You win!******************')

    print(stages[lives])