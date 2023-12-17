from deck import *
from collections import Counter

def straight_flush(hand,value_list,suit_list):
    #counts the occurrences of each suit
    suit_counts = Counter(card.suit for card in hand)
    #determins the most common card
    most_common_suit = suit_counts.most_common(1)[0][0] #idk what any of these brackets do 
    #makes a new list that only contains the cards of the most common suit
    same_suit_cards = [card for card in hand if card.suit == most_common_suit]
    
    if len(same_suit_cards) >= 5:
        values = [card.value for card in same_suit_cards]
        straight_f = straight(hand,list(set(values)),suit_list)
        if straight_f:
            return sorted(straight_f,reverse=True)

def four_kind(hand,value_list,suit_list):
    #same as pair but with 4
    ordered = sorted(value_list, reverse=True)
    for card in ordered:
        if ordered.count(card) == 4:
            return card
        
def full_house(hand,value_list,suit_list):
    ordered = sorted(value_list, reverse=True)
    full = []
    #first check for a 3 of a kind
    #had to rewrite it here as the function doesn't remove the duplicates
    for card in ordered:
        if ordered.count(card) == 3:
            full.extend([card,card,card])
            ordered = list(filter((card).__ne__, ordered))
            #if there is a 3 of a kind then it calls the pair function, if so then there is a full house
            yes = pair(hand,ordered,suit_list)
            if yes:
                full.extend([yes,yes])
                return full

def flush(hand,value_list,suit_list):
    for card in suit_list:
        if suit_list.count(card) == 5:
            return True

def straight(hand,value_list,suit_list):
    #makes a list that is ordered in decending order without any repeats
    ordered = sorted(set(value_list), reverse=True)
    count = 1
    straight = []
    #iterates through all items in the sorted list, it will start with the 2nd item
    for card in range(1, len(ordered)):
        #if the next item it 1 less then the current item then a straight starts
        if ordered[card] == ordered[card - 1] - 1:
            count += 1
            #append both current and next item
            straight.extend([ordered[card- 1],ordered[card]])
            if count == 5:
                #return the list without any duplicates
                return list(set(straight))
        else:
            count = 1
            straight = []
        
def three_kind(hand,value_list,suit_list):
    #same as pair but with 3
    ordered = sorted(value_list, reverse=True)
    for card in ordered:
        if ordered.count(card) == 3:
            return card
        
def two_pair(hand,value_list,suit_list):
    ordered = sorted(value_list, reverse=True)
    count = 0
    #same as pair but will not stop after finding one pair and will go through every item in the list
    for card in ordered:
        if ordered.count(card) == 2:
            #once a pair has been found it removes all duplicates of that value in the list
            ordered = list(filter((card).__ne__, ordered))
            count += 1
    if count == 2:
        return True
        
def pair(hand,value_list,suit_list):
    #orders the list of values in decending order
    ordered = sorted(value_list, reverse=True)
    #goes through each item in the list starting from the largest and see if it has any repeats
    for card in ordered:
        if ordered.count(card) >= 2:
            return card

def high_card(hand,value_list,suit_list):
    return max(value_list)

def check_hand(hand):
    #to check the hand, call this function which will then run other functions to then return the strongest hand
    value_list = []
    suit_list = []
    #this makes a list of cards by value and suit only so as not to be repeated in each function. functions that require value to be ordered can do so
    for card in hand:
        value_list.append(card.value)
        suit_list.append(card.suit)
    #list of all hand check functions
    hand_checks = [straight_flush, four_kind, full_house, straight, three_kind, two_pair, pair, high_card]
    
    for poker_check in hand_checks:
        result = poker_check(hand,value_list,suit_list)
        if result:
            return poker_check.__name__ , result