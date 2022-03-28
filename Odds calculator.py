# -*- coding: utf-8 -*-
"""
Poker Odds Calculator:
    The user can input two or three Texas Hold'em hole cards hands + any amount 
    of community cards (PF, Flop or Turn) and the program calculates the odds 
    of winning for each hand using brute force.
    The user can also choose how many times the program must run the cards to 
    calculate the odds (e.g. 10'000x, 100'000x, 200'000x, ...)

@author: Gun
"""

import Poker
from Input import *
import Cards

play = True
while play:
    deck = Poker.PokerDeck()
    num_players = get_integer("How many players? ")
    players = []
    for i in range(num_players):
        c1 = get_poker_card(f"Please enter the first card for Player {i+1}: ")
        c2 = get_poker_card(f"Please enter the second card for Player {i+1}: ")
        players.append(Poker.PokerPlayer((c1, c2)))
    board = Cards.Hand()
    if get_yes_or_no("Do you want to choose the flop? "):
        board.get_card(deck.deal(get_poker_card(f"Please enter the flop's first card: ")))
        board.get_card(deck.deal(get_poker_card(f"Please enter the flop's second card: ")))
        board.get_card(deck.deal(get_poker_card(f"Please enter the flop's third card: ")))
        print(f"--- The flop is: ---\n{str(board)}")
        if get_yes_or_no("Do you want to choose the turn? "):
            board.get_card(deck.deal(get_poker_card(f"Please enter the turn: ")))
            print(f"--- The turn is: ---\n{str(board)}")
    deck.shuffle()
    n = get_integer("How many simulations? ")
    # Flop
    for i in range(3):
        board.get_card(deck.deal())
    print(f"--- The flop is: ---\n{str(board)}")
    # Turn
    board.get_card(deck.deal())
    print(f"--- The turn is: ---\n{str(board)}")
    # River
    board.get_card(deck.deal())
    print(f"--- The river is: ---\n{str(board)}")
    winner = []
    for player in players:
        player.eval_poker_hand(board.cards)
        print(f"Player {players.index(player)+1} has:\n{str(player)}")
        if not winner:
            winner = [player]
        elif player.get_poker_hand() > winner[0].get_poker_hand():
            winner[0] = player
        elif player.get_poker_hand() == winner[0].get_poker_hand():
            winner.append(player)
    if len(winner) == 1:
        print(f"Player {players.index(winner[0])+1} wins!")
    else:
        text = f"Players {players.index(winner[0])+1} "
        for i in range(1,len(winner)):
            text += f"and {players.index(winner[i])+1} "
        text += f"split!"
        print(text)

    play = get_yes_or_no("Do you want to calculate new odds? ")
