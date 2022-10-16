from random import randint
from art import *

def play():
    cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    points = 0
    hand = []
    dealer_hand = []
    print("Here is the dealer's first card:")
    get_card( cards, dealer_hand)
    print("Here is your hand:")
    get_card(cards, hand)



def get_card(cards, hand):

    if len(hand) < 2:
        for i in range(2):
            card = cards[randint(0,13)]
            hand.append(card)
    else:
        for i in range(1):
            card = cards[randint(0,13)]
            hand.append(card)

    for c in range(len(hand)):
        tprint(hand[c],font="block",chr_ignore=True)
    return hand



