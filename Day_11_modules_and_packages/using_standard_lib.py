# # # # # # using Python standard library
# # # # # # https://docs.python.org/3/library/
# # # # # # Extensive - Batteries Included - just import!
# # # # # # Available across most OSes
#
# # # # # # 4 ways of importing modules
from datetime import datetime as dt # datetime has datetime submodule!
import string # mostly useful constants
import math
# # # # # import math as mth # Python likes these short names but not for standard library!
# # # # # from math import floor # i could import floor alone but beware name collission
# from math import factorial as fact
from collections import Counter # so i only want Counter from collections package
from statistics import mean
import random
import itertools
#
# # import mat_lib # this library comes from my own PYTHONPATH
#
# # print(mat_lib.add(3,76))
#
# # print(string.punctuation)
throws = 100_000
before = dt.now()
print(before)
# for i in range(100_000):
#     t = i*3
rand_dice = [random.randint(1,6) for _ in range(throws)] # _ because we do not need the variable
after = dt.now()

print(sum(rand_dice)/throws)
print(mean(rand_dice))  # mean is from statistics import mean
print(after)
delta = after - before # so this means time oject have __sub__ overloaded
print(delta)
print("Just seconds and microseconds of delta", delta.seconds, delta.microseconds)
print(after.year, after.day, after.weekday(), after.hour, after.minute, after.second )
print(string.ascii_lowercase)
print(math.factorial(5))
# # # # # print(mth.factorial(4))
# # # # # print(floor(3.98))
# # # # print(fact(6))
my_count = Counter("abracadabra")
print(my_count)  # this will be dictionary
print(my_count.most_common())
# # # # # # print(my_count.most_common(3))
# print(my_count.keys())
# print(list(my_count.keys()))
# print(my_count.values())
#
# # # # # # # print(type(my_count.most_common()))
# # # # # # print(my_count['a'])
# beg = dt.now()
# print(beg)
# ran_nums = [random.randint(1, 6)+random.randint(1, 6)
#             for _ in range(1_000_000)]
# end = dt.now()
# print(end)
# print(f"Took {end-beg} seconds")
# print(sum(ran_nums)/len(ran_nums))
# print(mean(ran_nums))
# # so i put all the throws in buckets (presumably from 2 to 12)
# ncount = Counter(ran_nums)
# print(ncount.most_common())

first = "ABC"
second = "01234"
cartesian_product = list(itertools.product(first, second))  # so like double loop for all x all
print(cartesian_product)

numbers = list(range(10))
new_shuffled = random.sample(numbers, 10)
print(new_shuffled)
# choices is not going to work here Return a k sized list of elements chosen from the population with replacement.
print(random.choices(numbers, k=10))  # so choices will give us duplicates, with replacement
print(numbers)
random.shuffle(numbers)  # IN PLACE so returns nothing
print(numbers)


