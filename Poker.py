from Cards import *


class Poker_Card(Card):
    def __init__(self, a_value, a_suit):
        """
        Parameters:
            - a_value: int between 1 and 13
            - a_suit: "s", "h", "d" or "c"
        ---
        Initialize card and adds:
            - a poker_value, 2 to 14
        ---
        Returns nothing.
        """
        super().__init__(a_value, a_suit)
        self.poker_value = 0 
        if self.id_value == 1 :
            self.poker_value = 14
        else:
            self.poker_value = self.id_value
    
    def __lt__(self, other):
        return self.poker_value < other.poker_value

    def __gt__(self, other):
        return self.poker_value > other.poker_value
    
    def __le__(self, other):
        return self.poker_value <= other.poker_value

    def __ge__(self, other):
        return self.poker_value >= other.poker_value


class Poker_Deck(Deck):
    def __init__(self):
        """
        Initiate the deck with poker cards.
        """
        self.cards = []
        for suit in suits:
            for id_value in range(len(values)):
                self.cards.append(Poker_Card(id_value + 1, suit))


class Poker_Hand(Hand):
    def __init__(self, cards = None):
        """
        Parameters:
            - cards : list of cards, optional. The default is None.
        ---
        Initialize the poker hand, adding the cards given if any.
        ---
        Returns nothing.
        """
        super().__init__()
        # container for cards by suits, for easier hand id        
        self.suits = {"s":[],"h":[],"d":[],"c":[]}
        # cards value counter, for easier hand id
        self.values = {}
        # initialize all poker values (2 to 14) to empty list
        for i in range(2,15):
            self.values[i] = []
        # best 5-cards han
        # tuple: (Hand type (10-0), List of 5 cards , "Description" )
        self.best_hand = (0, [], "No 5-cards hand yet")
        if cards:
            for card in cards:
                self.get_card(card)
    
    def __lt__(self, other):
        if self.best_hand[0] == other.best_hand[0]:
            #case if the hands are the same (e.g. straight vs straight)
            for i in range(5):
                if self.best_hand[1][i] < other.best_hand[1][i] or self.best_hand[1][i] > other.best_hand[1][i] :
                    return self.best_hand[1][i] < other.best_hand[1][i]
            # if the whole for loop is executed the hands are exactly the same
            return False
        else:
            return self.best_hand[0] < other.best_hand[0]

    def __gt__(self, other):
        if self.best_hand[0] == other.best_hand[0]:
            #case if the hands are the same (e.g. straight vs straight)
            for i in range(5):
                if self.best_hand[1][i] < other.best_hand[1][i] or self.best_hand[1][i] > other.best_hand[1][i] :
                    return self.best_hand[1][i] > other.best_hand[1][i]
            # if the whole for loop is executed the hands are exactly the same
            return False
        else:
            return self.best_hand[0] > other.best_hand[0]
    
    def __eq__(self, other):
        return not (self > other or self < other)

    def __repr__(self):
        """
        Represents the hand in 2 lines:
            - Line 1: Text description.
            - Line 2: Shows the cards.
        ---
        Returns a string.
        """
        string = ""
        string = self.best_hand[2] + "\n"
        for card in self.best_hand[1]:
            string += str(card)
        return string
    
    def __str__(self):
        """
        Represents the hand in 2 lines:
            - Line 1: Text description.
            - Line 2: Shows the cards.
        ---
        Returns a string.
        """
        string = ""
        string = self.best_hand[2] + "\n"
        for card in self.best_hand[1]:
            string += str(card)
        return string
    
    def description(self, a_num, cards):
        """
        Parameters:
            - a_num: integer between 1 and 10, identifies the hand type
            - cards: a list of 5 cards
        ---
        Helper function to evaluate. Describes the current best hand, e.g.:
            - "Flush, Ace High"
            - "Straight, Jack high"
            - "Full house, 5's full of 3's"
            - "Pair of Q's, T kicker"
            - "High card A, K kicker"
        ---
        Returns a string.
        """
        text = ""
        if a_num == 10 :
            text = "Royal flush"
        elif a_num == 9 :
            text = "Straight flush, " + cards[0].symbol + " high."
        elif a_num == 8 :
            text = "Quads " + cards[0].symbol + "'s, kicker " + cards[-1].symbol + "."
        elif a_num == 7 :
            text = "Full house, " + cards[0].symbol + "'s full of " + cards[3].symbol + "'s."
        elif a_num == 6 :
            text = "Flush, " + cards[0].symbol + " high."
        elif a_num == 5 :
            text = "Straight, " + cards[0].symbol + "high."
        elif a_num == 4 :
            text = "Trips " + cards[0].symbol + "'s, kicker " + cards[3].symbol + "."
        elif a_num == 3 :
            text = ("Two pairs, " + cards[0].symbol + "'s and " + cards[2].symbol
                    + "'s, kicker " + cards[-1].symbol + ".")
        elif a_num == 2 :
            text = "A pair of " + cards[0].symbol + "'s, kicker " + cards[2].symbol + "."
        elif a_num == 1 :
            text = "High card " + cards[0].symbol + ", kicker " + cards[0].symbol + "."
        return text

    def evaluate(self):
        """
        Evaluates itself to determine what is currently the best 5-cards hand.
        Does nothing if there are less than 5 cards in the hand.
        Update self.best_hand 
        ---
        Returns nothing.
        """
        if len(self.cards) >= 5 : 
            calls = {10 : self.is_royal_flush ,
                      9 : self.is_straight_flush ,
                      8 : self.is_quads ,
                      7 : self.is_full_house ,
                      6 : self.is_flush ,
                      5 : self.is_straight ,
                      4 : self.is_trips ,
                      3 : self.is_two_pairs ,
                      2 : self.is_pair ,
                      1 : self.high_card }
            for i in range(10, 0, -1):
                current = calls[i]()
                if current:
                    self.best_hand = (i, current, self.description(i, current))
                    break

    def get_card(self, a_card):
        super().get_card(a_card)
        # sort the cards in reverse order by their poker_value
        self.cards.sort(key=lambda card : card.poker_value , reverse = True)
        # update values
        self.values[a_card.poker_value].append(a_card)
        # update suits
        self.suits[a_card.suit].append(a_card)
        self.suits[a_card.suit].sort(key=lambda card : card.poker_value , reverse = True)
        # evaluate hand to determine new current best hand
        self.evaluate()
        
    def high_card(self):
        """
        Returns:
            - if at least 5 cards: the 5 highest cards.
            - otherwise: empty list
        """
        high_card = []
        if len(self.cards) >= 5 :
            high_card = self.cards[0:5]
        return high_card
                
    def is_straight(self, some_cards = None):
        """
        Paramenters:
            - some_cards: a list of poker cards. Default: self.cards
        ---
        Checks if there is a straight.
        ---
        Returns: 
            - if found : the 5 cards that form the highest straight.
            - if not found : an empty list
        """
        straight = []
        if not some_cards:
            some_cards = self.cards.copy()
        if len(some_cards) >= 5:
            some_cards.sort(key=lambda card : card.poker_value , reverse = True)
            current = []
            for card in some_cards:
                if not current:
                    current.append(card)
                elif card.poker_value == current[-1].poker_value - 1 :
                    current.append(card)
                elif card.poker_value != current[-1].poker_value :
                    current.clear()
                    current.append(card)
                if len(current) == 5:
                    straight = current
                    break
                elif len(current) == 4 and current[-1].poker_value == 2 and some_cards[0].poker_value == 14:
                    current.append(some_cards[0])
                    straight = current
                    break
        return straight

    def is_flush(self):
        """
        Checks if the hand has a flush.
        ---
        Returns:
            - if found: the 5 highest cards with the same suit
            - if not: an empty list
        """
        flush = []
        if len(self.cards) >= 5 :
            for suit in self.suits:
                if len(self.suits[suit]) >= 5:
                    if not flush:
                        for i in range (5):
                            flush.append(self.suits[suit][i])
                    else:
                        for i in range(len(flush)):
                            if flush[i].poker_value < self.suits[suit][i].poker_value:
                                flush.clear()
                                for j in range (5):
                                    flush.append(self.suits[suit][j])
                                break
                            elif flush[i].poker_value > self.suits[suit][i].poker_value:
                                break
        return flush

    def is_royal_flush(self):
        """
        Checks if the hand has a royal flush.
        ---
        Returns:
            - if found: the 5 cards that forms a royal flush
            - if not: an empty list
        """
        royal = []
        flush = self.is_flush()
        if flush:
            if flush[0].poker_value == 14 and flush[-1].poker_value == 10:
                royal = flush                    
        return royal
    
    def is_straight_flush(self):
        """
        Checks if the hand has a straight flush.
        ---
        Returns:
            - if found: the 5 cards that forms a straight flush
            - if not: an empty list
        """        
        straight_flush = []
        flush = self.is_flush()
        if flush:
            straight_flush = self.is_straight(flush)
        return straight_flush
    
    def is_quads(self):
        """
        Checks if the hand has quads.
        ---
        Returns:
            - if found: 5 cards, the 4 cards that forms quads + highest next card
            - if not: an empty list
        """
        quads = []
        if len(self.cards) >= 5:
            for value in self.values:
                if len(self.values[value]) == 4:
                    quads = self.values[value].copy()
            if quads :
                for card in self.cards:
                    if card > quads[0] or card < quads[0] :
                        quads.append(card)
                        break
        return quads
    
    def is_trips(self):
        """
        Checks if the hand has trips.
        ---
        Returns:
            - if found: 5 cards, the 3 cards that forms trips + the 2 next highest cards
            - if not: an empty list
        """
        trips = []
        if len(self.cards) >= 5 :
            for value in self.values:
                if len(self.values[value]) == 3:
                    trips = self.values[value].copy()
            if trips :
                for card in self.cards:
                    if card > trips[0] or card < trips[0] :
                        trips.append(card)
                    if len(trips) == 5 :
                        break
        return trips
    
    def is_pair(self):
        """
        Checks if the hand has a pair.
        ---
        Returns:
            - if found: 5 cards, the pair + the 3 next highest cards
            - if not: an empty list
        """
        pair = []
        if len(self.cards) >= 5 :
            for value in self.values:
                if len(self.values[value]) == 2:
                    pair = self.values[value].copy()
            if pair :
                for card in self.cards:
                    if card > pair[0] or card < pair[0] :
                        pair.append(card)
                    if len(pair) == 5 :
                        break
        return pair
    
    def is_full_house(self):
        """
        Checks if the hand has a full house.
        ---
        Returns:
            - if found: 5 cards, the trips + the pair
            - if not: an empty list
        """
        fh = []
        if len(self.cards) >= 5 :
            trips = []
            highest_pair = []
            # collect all trips and pairs
            for value in self.values:
                if len(self.values[value]) == 3:
                    trips += self.values[value]
                if len(self.values[value]) == 2:
                    highest_pair += self.values[value]
            if len(trips) >= 3 :    # there is at least 1 trips
                if len(trips) >= 6 :    # there are at least 2 trips
                    if highest_pair :   # there is also at least a pair
                        #check if pair is higher than second trips' card
                        if highest_pair[-1] > trips[-4] :
                            fh = trips[-3:] + highest_pair[-2:]
                        else:   # takes second trips as pair
                            fh = trips[-3:] + trips[-5:-3]
                    else:
                        fh = trips[-3:] + trips[-5:-3]
                elif highest_pair :
                    fh = trips[-3:] + highest_pair[-2:]
        return fh
    
    def is_two_pairs(self):
        """
        Checks if the hand has two pairs.
        ---
        Returns:
            - if found: 5 cards, the 2 pairs + the next highest card
            - if not: an empty list
        """
        two_pairs = []
        if len(self.cards) >= 5 :
            pairs = []
            for value in self.values:
                if len(self.values[value]) == 2:
                    pairs += self.values[value]
            if len(pairs) >= 4 :
                for i in range(4):
                    two_pairs.append(pairs.pop())
            if two_pairs:
                for card in self.cards:
                    if (card > two_pairs[0] or card < two_pairs[0]) and (
                        card > two_pairs[-1] or card < two_pairs[-1] ) :
                        two_pairs.append(card)
                        break
        return two_pairs
    
    

