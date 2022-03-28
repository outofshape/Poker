from Poker import *
def yes_or_no(a_question):
    reply = input(a_question+" (y/n): ")
    if reply == "y":
        return True
    elif reply == "n":
        return False
    else:
        print("Please answer with y or n.")
        return yes_or_no(a_question)

answer = True
while answer:
    deck = Poker_Deck()
    deck.shuffle()
    ph1 = Poker_Hand()
    ph2 = Poker_Hand()
    for i in range(5):
        ph1.get_card(deck.deal())
        ph2.get_card(deck.deal())
    print("--- New Hand ---\n")
    print("Player 1 has the following cards:")
    string = ""
    for card in ph1.cards:
        string += str(card)
    print(string)
    print("Player 1's hand:")
    print(ph1)
    print("")
    print("Player 2 has the following cards:")
    string = ""
    for card in ph2.cards:
        string += str(card)
    print(string)
    print("Player 2's hand:")
    print(ph2)
    print("")
    if ph1 > ph2:
        print("Player 1 wins!")
    elif ph2 > ph1:
        print("Player 2 wins!")
    else:
        print("It's a draw!")
    answer=yes_or_no("Do you want to play again?")
