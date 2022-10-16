from random import randint
from art import *
from utils import *

cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
x = 0
for value in cards:
    if x < 42:
        cards.append(value)
    else:
        break
    x += 1

tprint("Blackjack",font="block",chr_ignore=True)

print("Do you want to play? Y or N")
answer = input().lower

if answer() == "y":
    play(cards)
else:
    exit()