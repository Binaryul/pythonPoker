from deck import *


def straight_flush():
    pass

def four_kind(hand):
    for card in hand:
        if hand.count(card.value) == 4:
            return True
            break
        
def full_house():
    pass

def flush():
    pass

def straight():
    pass
        
def three_kind(hand):
    for card in hand:
        if hand.count(card.value) == 3:
            return True
            break
        
def two_pair():
    pass
        
def pair(hand):
    for card in hand:
        if hand.count(card.value) == 2:
            return True
            break



def check_hand():
    pass