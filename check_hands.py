from deck import *

def straight_flush(hand):
    pass

def four_kind(hand):
    #same as pair but with 4
    ordered = sorted(hand, reverse=True)
    for i in ordered:
        if ordered.count(i) == 4:
            return True
        
def full_house(hand):
    pass

def flush(hand):
    pass

def straight(hand):
    pass
        
def three_kind(hand):
    #same as pair but with 3
    ordered = sorted(hand, reverse=True)
    for i in ordered:
        if ordered.count(i) == 3:
            return True
        
def two_pair(hand):
    ordered = sorted(hand, reverse=True)
    count = 0
    #same as pair but will not stop after finding one pair and will go through every item in the list
    #once a pair has been found it removes all duplicates of that value in the list
    for i in ordered:
        if ordered.count(i) == 2:
            ordered = list(filter((i).__ne__, ordered))
            count += 1
    if count == 2:
        return True
        
def pair(hand):
    #orders the list of values in decending order
    ordered = sorted(hand, reverse=True)
    #goes through each item in the list starting from the largest and see if it has any repeats
    for i in ordered:
        if ordered.count(i) == 2:
            return True



def check_hand(hand):
    #to check the hand, call this function which will then run other functions to then return the strongest hand
    value_list = []
    suit_list = []
    #this makes a list of cards by value and suit only so as not to be repeated in each function. functions that require value to be ordered can do so
    for card in hand:
        value_list.append(card.value)
        suit_list.append(card.suit)
    t = pair(value_list)
    return t




#test
hand = [Card(4,"Clubs"),Card(4,"Diamonds"),Card(5,"Spades"),Card(7,"Hearts"),Card(7,"Clubs")]

t = check_hand(hand)
if t == True:
    print("skdfjh")
    
