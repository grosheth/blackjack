from random import randint
from art import *
from utils import *

tprint("Blackjack",font="block",chr_ignore=True)

print("Do you want to play? Y or N")
answer = input().lower

if answer() == "y":
    play()
else:
    exit()