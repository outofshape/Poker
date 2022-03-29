from random import *

suits= ("s","h","d","c")
values= ("A","2","3","4","5","6","7","8","9","T","J","Q","K")

class Card:
    def __init__(self, a_value, a_suit):
        assert 0 < a_value <= len(values), "Card value must be between 1 and 13"
        assert a_suit in suits, "suit is not 'd','h','s' or 'c'"
        self.suit = a_suit
        self.id_value = a_value
        self.symbol = values[a_value-1]

    def __str__(self):
        return "|" + self.symbol + self.suit + "| "
    
    def __repr__(self):
        return "|" + self.symbol + self.suit + "| "

    def __eq__(self, other):
        return self.id_value == other.id_value and self.suit == other.suit

    def __lt__(self, other):
        return self.id_value < other.id_value

    def __gt__(self, other):
        return self.id_value > other.id_value
    
    def __le__(self, other):
        return self.id_value <= other.id_value

    def __ge__(self, other):
        return self.id_value >= other.id_value
    
    
class Hand:
    def __init__(self, cards=None):
        self.cards = []
        if cards:
            self.cards = cards.copy()

    def get_card(self, a_card):
        if not a_card:
            pass
        else:
            self.cards.append(a_card)

    def get_number_of_cards(self):
        return len(self.cards)

    def search(self, a_card):
        """
        Search a_card in the hand. If found returns the card, otherwise returns None.
        """
        if not self.cards :
            print("Hand has no cards!")
            return None
        else:
            found = None
            for card in self.cards:
                if card == a_card:
                    found = card
            return found
    
    def give_card(self, a_card = None):
        """
        Pop and returns the card given as argument. If not in the hand returns None.
        If no card is given as argument, pop and returns last card.
        """
        if not self.cards:
            print("Hand has no cards!")
            return None
        elif not a_card:
            return self.cards.pop()
        else:
            found = self.search(a_card)
            if not found:
                return found
            else:
                self.cards.remove(found)
                return found

    def __str__(self):
        string= ""
        for card in self.cards:
            string += str(card)
        return string


class Deck(Hand):
    def __init__(self, cards=None):
        super().__init__(cards)
        if not self.cards:
            for suit in suits:
                for id_value in range(len(values)):
                    self.cards.append(Card(id_value + 1, suit))

    def shuffle(self):
        temp = []
        seed()
        while len(self.cards) > 0:
            temp.append(self.cards.pop(randrange(len(self.cards))))
        self.cards = temp

    def deal(self, a_card=None):
        """
        Parameters:
            - a_card: Card (optional). 
        ---
        If specified returns the given card from the deck, if present.
        Otherwise returns the last card of the deck.
        ---
        Returns: - None if deck is empty or card not found. 
                - a_card or last card in the deck otherwise.
        """
        if not self.cards:
            print("The deck is empty!")
            return None
        elif not a_card:
            return self.cards.pop()
        else: 
            found = self.search(a_card)
            if not found:
                return found
            else:
                self.cards.remove(found)
                return found
