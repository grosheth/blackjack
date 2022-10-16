from curses.ascii import isdigit
from random import randint
from art import *

def play():
    cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    x = 0
    for value in cards:
        if x < 42:
            cards.append(value)
        else:
            break
        x += 1
    
    print(cards)
    points = 0
    dealer_points = 0
    hand = []
    dealer_hand = []
    print("Here is the dealer's first card:")
    get_card_dealer(cards, dealer_hand)
    print("Here is your hand:")
    get_card(cards, hand)
    points = convert(hand, points)
    dealer_points = convert(dealer_hand, dealer_points)
    while True:
        print(f"you currently have {points}")
        print(f"The dealer has {dealer_points}")
        print("1. Get another card.")
        print("2. Stand with current cards.")
        answer = input()

        if answer == "1":
            print("Here is your hand:")
            get_card(cards, hand)
            points = convert(hand, points)
            if points > 21:
                print("You have more than 21, you lost")
                print("1: Replay    2: Quit")
                exit()
            win = decision(points, dealer_points)
            if win:
                print(f"You won with {points} against the dealer's {dealer_points}")
                
        elif answer == "2":
            print("Here is the dealer's hand")
            get_card_dealer(cards, dealer_hand)
            dealer_points = convert(dealer_hand, dealer_points)
            if dealer_points > 21:
                print("You Won the dealer has more than 21")
                print("1: Replay    2: Quit")
                exit()
        else:
            print("invalid answer")


def get_card_dealer(cards, dealer_hand):

    card = cards[randint(len(cards))]
    cards.pop(card)
    print(cards)
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
    print(points)
    print(hand)
    if points > 0:
        if hand[-1].isdigit():
            c = int(hand[-1])
        else:
            if hand[-1] != "A":
                c = 10
            elif points < 21:
                c = 11
            else:
                c = 1
        print(c)
        points += c
    else:
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

def decision(points, dealer_points):
    if points > dealer_points:
        win = True
        return win
    else:
        win = False
        return win