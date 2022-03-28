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
import tkinter as tk

class Player():
    def __init__(self, a_name):
        self.name = a_name
        self.hole_cards = []
        self.hand = pkr.Poker_Hand()
        self.wins = 0
    
    def __str__(self):
        string = self.name + " "
        for card in self.hole_cards:
            string += str(card)
        return string

def clickedCardBtn():
    

window = tk.Tk()
window.title("Odds Calculator")
window.geometry('350x200')

greeting = tk.Label(window, text="Welcome to the odds calculator!")
greeting.pack()

lbl_hands = tk.Label(window, text= "Please choose the cards for Player 1:")
lbl_hands.pack()

card_back = tk.PhotoImage(file = "card_back.png")
btn_c1 = tk.Button(window, image= card_back, height=50, width=0.67*50)
btn_c1.pack(side=tk.LEFT)
btn_c2 = tk.Button(window, image= card_back, height=50, width=0.67*50)
btn_c2.pack(side=tk.LEFT)

window.mainloop()

