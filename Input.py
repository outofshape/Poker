# -*- coding: utf-8 -*-
"""
Functions to handle different kind of inputs

@author: Gun
"""
import Cards


def get_yes_or_no(message):
    reply = input(message + " (y/n): ")
    if reply == "y":
        return True
    elif reply == "n":
        return False
    else:
        print("Please answer with y or n.")
        return get_yes_or_no(message)


def get_integer(message="Please enter an integer:"):
    while True:
        try:
            reply = int(input(message))
            return reply
        except ValueError:
            print('You must enter an integer')


def get_card(message):
    while True:
        try:
            reply = input(message + " e.g. Kd, 8s,.. : ")
            card = Cards.Card(Cards.values.index(reply[0])+1, reply[1])
            return card
        except (AssertionError, TypeError, IndexError, ValueError):
            pass
