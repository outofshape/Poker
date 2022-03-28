# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:27:55 2020

Poker Odds Calculator:
    The user can input two or three Texas Hold'em hole cards hands + any amount 
    of community cards (PF, Flop or Turn) and the program calculates the odds 
    of winning for each hand using brute force.
    The user can also choose how many times the program must run the cards to 
    calculate the odds (e.g. 10'000x, 100'000x, 200'000x, ...)

@author: Gun
"""

import Poker as pkr
from Input import *

play = True
while play:


    play = get_yes_or_no("Do you want to play again?")