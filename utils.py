from curses.ascii import isdigit
from random import randint
from art import *

def play():
    cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    points = 0
    hand = []
    dealer_hand = []
    print("Here is the dealer's first card:")
    get_card_dealer(cards, dealer_hand)
    print("Here is your hand:")
    get_card(cards, hand)
    points = convert(hand, points)
    while True:
        print(f"you currently have {points}")
        print("1. Get another card.")
        print("2. Keep current cards.")
        answer = input()

        if answer == "1":
            print("Here is your hand:")
            get_card(cards, hand)
        elif answer == "2":
            print("Here is the dealer's hand")
            get_card_dealer(cards, dealer_hand)
        else:
            print("invalid answer")


def get_card_dealer(cards, dealer_hand):

    card = cards[randint(0,13)]
    dealer_hand.append(card)
    if len(dealer_hand) < 2:
        for c in range(len(dealer_hand)):
            tprint(dealer_hand[c],font="block",chr_ignore=True)
            tprint(" ",font="block",chr_ignore=True)
    else:
        for c in range(len(dealer_hand)):
            tprint(dealer_hand[c],font="block",chr_ignore=True)
    return dealer_hand

def get_card(cards, hand):

    if len(hand) < 2:
        for i in range(2):
            card = cards[randint(0,13)]
            hand.append(card)
    else:
        card = cards[randint(0,13)]
        hand.append(card)

    for c in range(len(hand)):
        tprint(hand[c],font="block",chr_ignore=True)
    return hand


def convert(hand, points):
    for c in hand:
        if c.isdigit():
            c = int(c)
        else:
            if c != "A":
                c = 10
            elif points < 21:
                c = 11
            else:
                c = 1
        print(c)
        points += c
    print(points)
    return points

