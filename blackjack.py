import random

# Start
# Deal cards to user and computer user: [1 card, 2 card], computer's first card is x
# Create a deal function, gets random cards

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    print(card)
    return card
deal()