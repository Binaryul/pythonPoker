from deck import *
import random

deck = create_deck()

shuffled = random.sample(deck, len(deck))

class Players:
    def __init__(self, bank, name):
        self.bank = bank
        self.cards = []
        self.name = name
    #when printed the name of the player is printed
    def __repr__(self):
        return self.name
    #function to add to the list of cards in the class
    def draw(self, current_card):
        self.cards.extend(current_card)
    
    def bet(self,bet):
        self.bank = self.bank - bet
    

play_count = 5

#draws cards from the deck, made to be used in different projects
def draw(num_cards):
    drawn_cards = []
    for i in range(num_cards):
        drawn_cards.append(shuffled[0])
        shuffled.pop(0)
    return drawn_cards

def deal(name,bank, Sblind):
    CPU = []
    players = []
    #creates all the computers based on the player count and gives them names 
    for i in range(play_count - 1):
        CPU.append(Players(bank,f"CPU_{i+1}"))
    
    player = Players(bank, name)
    
    players.extend(CPU)
    players.append(player)
    
    for name in players:
        drawn = draw(2)
        name.draw(drawn)
    
    blinds(players,Sblind)
    
def blinds(players,Sblind):
    players[0].bank -= Sblind
    players[1].bank -= Sblind*2

    
deal("Binamra",1000,2)
