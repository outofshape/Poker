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


def calculate_odds(players, board, deck, n):
    """
    Calculates the odds of winning for each player's hands, by running the remaining cards "n" times randomly.

    :param players: List of PokerPlayers
    :param board: Cards.Hand object, can have 0, 3 (Flop) or 4 (Turn) cards
    :param deck: PokerDeck with the remaining cards
    :param n: Integer
    :return: List of Dict [{wins: #, losses: #}, {wins: #, losses: #}, {wins: #, losses: #}, ...]
    """
    results = []
    for p in range(len(players)):
        results.append({"wins": 0, "losses": 0})
    for iterations in range(n):
        t_board = Cards.Hand(board.cards)
        t_deck = Poker.PokerDeck(deck.cards)
        t_deck.shuffle()
        for j in range(5-board.get_number_of_cards()):
            t_board.get_card(t_deck.deal())
        print(f"--- The board is: ---\n{str(t_board)}")
        w_index = []
        for player in players:
            p_i = players.index(player)
            player.eval_poker_hand(t_board.cards)
            print(f"Player {p_i + 1} has:\n{str(player)}")
            if not w_index:
                w_index.append(p_i)
            elif player.get_poker_hand() > players[w_index[0]].get_poker_hand():
                for w_i in w_index:
                    results[w_i]["losses"] += 1
                w_index = [p_i]
            elif player.get_poker_hand() == players[w_index[0]].get_poker_hand():
                w_index.append(p_i)
            else:
                results[p_i]["losses"] += 1
        if len(w_index) == 1:
            w_i = w_index[0]
            print(f"Player {w_i + 1} wins!")
            results[w_i]["wins"] += 1
        else:
            text = f"Players {w_index[0] + 1} "
            for w in range(1, len(w_index)):
                text += f"and {w_index[w] + 1} "
            text += f"split!"
            print(text)
    return results


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
    n = get_integer("How many simulations? ")
    results = calculate_odds(players, board, deck, n)
    for r in range(len(results)):
        wins = results[r]["wins"]
        losses = results[r]["losses"]
        print(f"Player {r+1} has {wins} Wins, {losses} Losses and a {wins*100/n}% chance of winning.")
    play = get_yes_or_no("Do you want to calculate new odds? ")
