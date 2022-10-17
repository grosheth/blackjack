from curses.ascii import isdigit
from random import randint
from art import *
import time

def play(cards):
    points = 0
    dealer_points = 0
    hand = []
    dealer_hand = []

    print("Here is the dealer's first card:")
    get_card_dealer(cards, dealer_hand)
    print("-------------------------------------")
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
                print("you have more than 21!")
                tprint("YOU LOST")
                exit()
                
        elif answer == "2":
                print("Here is the dealer's hand")
                get_card_dealer(cards, dealer_hand)
                print("-------------------------------------")
                dealer_points = convert(dealer_hand, dealer_points)
                time.sleep(1)

                while True:
                    
                    if dealer_points > 21:
                        print("You Won the dealer has more than 21")
                        tprint("YOU WON")
                        exit()

                    if dealer_points <= 16:
                        get_card_dealer(cards, dealer_hand)
                        dealer_points = convert(dealer_hand, dealer_points)
                        time.sleep(1)
                    else:
                        win = decision(points, dealer_points)

                        if win:
                            print(f"You won with {points} against the dealer's {dealer_points}")
                            tprint("YOU WON")
                            exit()
                        else:
                            print(f"You lost with {points} against the dealer's {dealer_points}")
                            tprint("YOU LOST")
                            exit()
        else:
            print("invalid answer")


def get_card_dealer(cards, dealer_hand):

    dealer_hand = pop_card(cards, dealer_hand)

    if len(dealer_hand) < 2:
        for c in range(len(dealer_hand)):
            tprint(dealer_hand[c],font="block",chr_ignore=True)
            tprint(".",font="block",chr_ignore=True)
    else:
        for c in range(len(dealer_hand)):
            tprint(dealer_hand[c],font="block",chr_ignore=True)
    return dealer_hand

def get_card(cards, hand):

    if len(hand) < 2:
        for i in range(2):
            hand = pop_card(cards, hand)
    else:
        hand = pop_card(cards, hand)

    for c in range(len(hand)):
        tprint(hand[c],font="block",chr_ignore=True)
    return hand


def pop_card(cards, hand):
    position = randint(0,len(cards))
    card = cards[position]
    cards.pop(position)
    hand.append(card)
    return hand

def convert(hand, points):
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
            points += c
    return points

def decision(points, dealer_points):
    if points == 21:
        win = True   
    elif points > dealer_points:
        win = True
        return win
    else:
        win = False
        return win