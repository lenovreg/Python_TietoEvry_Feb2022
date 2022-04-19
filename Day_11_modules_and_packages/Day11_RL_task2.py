import random
import itertools

class Deck:
    first = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    second = ["J", "Q", "K", "A"]
    numbers = list(range(2, 10))
    def __init__(self):
        self.available = list(itertools.product(self.first,self.second,self.numbers))
        self.shuffle()
        self.spent=[]

    def shuffle(self):
        self.available = random.sample(self.available,len(self.available))
        return self.available

    def get_cards(self,count=1):
        self.spent.extend(self.available[:count])
        self.available = self.available[count:]
        return self.spent,self.available

my_deck=Deck()
print(my_deck)
print(my_deck.shuffle())
spent,available=my_deck.get_cards(2)
print('Spent cards:',spent,'Available cards:',available)