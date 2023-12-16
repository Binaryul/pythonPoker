from deck import *

def straight_flush(hand):
    pass

def four_kind(hand):
    #same as pair but with 4
    ordered = sorted(hand, reverse=True)
    for card in ordered:
        if ordered.count(card) == 4:
            return card
        
def full_house(hand):
    ordered = sorted(hand, reverse=True)
    #first check for a 3ofAkind
    #had to rewrite it here as the function doesn't remove the duplicates
    for card in ordered:
        if ordered.count(card) == 3:
            ordered = list(filter((card).__ne__, ordered))
            #if there is a 3 of a kind then it calls the pair function, if so then there is a full house
            yes = pair(ordered)
            if yes:
                return True

def flush(hand):
    for card in hand:
        if hand.count(card) == 5:
            return True

def straight(hand):
    ordered = sorted(hand, reverse=True)
    count = 1
    straight = []
    #iterates through all items in the sorted list
    for card in enumerate(ordered):
        #if the next item = current + 1 increase the count
        if ordered[card+1] == ordered[card] + 1:
            count += 1
            straight.append(ordered[card])
            #if the count =5 then there are 5 items in numerical order
            if count == 5:
                #if there are a 5 items in numerical order, it returns the list of the straight to be compared later
                return straight
        else:
            #if the next item is not in numerical order then reset the count to 1
            straight.clear
            count = 1
        
def three_kind(hand):
    #same as pair but with 3
    ordered = sorted(hand, reverse=True)
    for card in ordered:
        if ordered.count(card) == 3:
            return card
        
def two_pair(hand):
    ordered = sorted(hand, reverse=True)
    count = 0
    #same as pair but will not stop after finding one pair and will go through every item in the list
    for card in ordered:
        if ordered.count(card) == 2:
            #once a pair has been found it removes all duplicates of that value in the list
            ordered = list(filter((card).__ne__, ordered))
            count += 1
    if count == 2:
        return True
        
def pair(hand):
    #orders the list of values in decending order
    ordered = sorted(hand, reverse=True)
    #goes through each item in the list starting from the largest and see if it has any repeats
    for card in ordered:
        if ordered.count(card) == 2:
            return card

def high_card(hand):
    return max(hand)

def check_hand(hand):
    #to check the hand, call this function which will then run other functions to then return the strongest hand
    value_list = []
    suit_list = []
    #this makes a list of cards by value and suit only so as not to be repeated in each function. functions that require value to be ordered can do so
    for card in hand:
        value_list.append(card.value)
        suit_list.append(card.suit)
    t = full_house(value_list)
    return t





#test
hand = [Card(2,"Clubs"),Card(2,"Clubs"),Card(2,"Clubs"),Card(3,"Clubs"),Card(3,"Diamond")]

t = check_hand(hand)
if t == True:
    print("skdfjh")
    
