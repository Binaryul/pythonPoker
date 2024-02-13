from players import *
from check_hands import check_hand, high_card

prefered_name = input("Enter the name you would like to play as: ")
prefered_bank = int(input("Enter your prefered staring balance (this will be consistant among all bots and yourself): "))
Sblind = round(prefered_bank*0.05)
print(f"The small blind will be calcualted as 5% of the bank being {Sblind}")

players = create_players(prefered_name,prefered_bank)

#deck created in players.py
#draws 5 cards to act as the global cards
global_cards = draw(5)





#test

deal(players,Sblind)
for name in players:
    print(name,name.bank, name.cards)