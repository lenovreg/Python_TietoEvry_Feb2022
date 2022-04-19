import random
import itertools

# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]
# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
# task1
def get_shuffled_cards():
    first=["diamonds ♦","hearts ♥","spades ♠","clubs ♣"]
    second=["J","Q","K","A"]
    numbers = list(range(2,10))
    print(numbers)
    numbers_third=random.randint(0,51)
    print(numbers_third)
    cartesian_product = list(itertools.product(first, second, numbers))
    print('All cards:' ,cartesian_product)
    return numbers_third, cartesian_product[numbers_third]
print('Random card',get_shuffled_cards())