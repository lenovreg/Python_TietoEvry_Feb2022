import random
import itertools

def main():
    print("running main_program.py residing at ", __file__)
    print("of course name is ", __name__)

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

if __name__ == "__main__":
    main()
    print("This will run when different.py is called normally")
else: # generally you do not need this else when importing
    print("I was imported! My __main__ is", __name__)
