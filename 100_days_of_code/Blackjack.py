import random

def deal_card():
    '''Returns random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score():
    user_scr = sum(user_cards)
    computer_scr = sum(computer_cards)
    return user_scr, computer_scr

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card)
    computer_cards.append(deal_card)

