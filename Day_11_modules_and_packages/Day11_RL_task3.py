import different as mm

my_deck=mm.Deck()
print(my_deck)
print(my_deck.shuffle())
spent,available=my_deck.get_cards(2)
print('Spent cards:',spent,'Available cards:',available)