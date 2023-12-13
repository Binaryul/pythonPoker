values = list(range(2,15))
suits = ["Clubs", "Diamonds", "Spades", "Hearts"]

#faceC is a dictionary to convert face cards to value and vice versa
faceC = {
    11:"J",
    12:"Q",
    13:"K",
    14:"A",
}

#class that holds the value and the suit of a deck to be called upon later
#note all number cards are in an integer form so no need to use a dictionary to convert to a value
#__str__ function allows the cards to be printed and have readable output
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        #checks if the value of the card is in the dictionary
        if self.value in faceC:
            #if so it then assigns that value the appropriate face card but only when it is printed
            value = faceC[self.value]
        else:
            value = self.value
        return f"{value} of {self.suit}"
        #this allows for nice formating when printing the cards but allows cards to be compared easily later
    
    
#fuction to create a deck
def deck(values, suits):
    cards = []
    for suit in suits:
        for value in values:
            cards.append(Card(value, suit))
    return cards
            
#function to be called on other files so as not to repeat value and suit lists    
def create_deck():
    p = deck(values, suits)
    return p

