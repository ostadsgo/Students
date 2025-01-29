"""
DESCRIPTION:
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""


# Kidos solve it like this
def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2

    return total


assert square_sum([1,2]) == 5
assert square_sum([0, 3, 4, 5]) == 50
assert square_sum([]) == 0
assert square_sum([-1,-2]) == 5
assert square_sum([-1,0,1]) == 2




# Programming gods solve it like this
def square_sum(numbers):
    return sum(num ** 2 for num in numbers)

assert square_sum([1,2]) == 5
assert square_sum([0, 3, 4, 5]) == 50
assert square_sum([]) == 0
assert square_sum([-1,-2]) == 5
assert square_sum([-1,0,1]) == 2