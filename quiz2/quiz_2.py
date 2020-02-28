# Written by *** and Eric Martin for COMP9021


from random import seed, shuffle
import sys
import time


# for_seed is meant to be an integer, length a strictly positive integer.
# length will not be large for most tests, but can be as large as 10_000_000.
def generate_permutation(for_seed, length):
    seed(for_seed)
    values = list(range(1, length + 1))
    shuffle(values)
    return values


def maps_to(values, x):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    return values.index(x)+1


def length_of_cycle_containing(values, x):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    result = values.index(x)+1
    length = 1
    while result != x:
        result = values.index(result)+1
        length += 1
    return length
        



# Returns a list of length len(values) + 1, with 0 at index 0
# and for all x in {1, ..., len(values)}, the length of the cycle
# containing x at index x.
def analyse(values):
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    result = [0]
    for x in values:
        result.append(length_of_cycle_containing(values, x))
    return result



start = time.time()
values=analyse(generate_permutation(1,10000000))
end=time.time()
print(end - start)
