"""
DESCRIPTION:
Given two integers a and b, which can be positive or negative, find the sum of all 
the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""

# kids way to do it
def get_sum(a,b):
    total = 0
    if a < b:
        for i in range(a, b+1):
            total += i
    elif a > b:
        for i in range(b, a+1):
            total += i
    else:
        total = a
    return total


# tests
assert get_sum(0, 1) == 1
assert get_sum(0, -1) == -1
assert get_sum(-1, 2) == 2
assert get_sum(5, 1) == 15
assert get_sum(1, 1) == 1



# Pros way to do it
def get_sum(a,b):
    a, b = sorted([a, b])
    return a if a == b else sum(range(a, b+1))

# tests
assert get_sum(0, 1) == 1
assert get_sum(0, -1) == -1
assert get_sum(-1, 2) == 2
assert get_sum(5, 1) == 15
assert get_sum(1, 1) == 1


# GODs way to do it
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

# tests
assert get_sum(0, 1) == 1
assert get_sum(0, -1) == -1
assert get_sum(-1, 2) == 2
assert get_sum(5, 1) == 15
assert get_sum(1, 1) == 1