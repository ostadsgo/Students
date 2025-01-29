import math

"""
cpt = 0
for i in range(4):
    cpt += i // 2 + 1
# print(cpt)
"""


def draw_shape(n, sep):
    for i in range(n + 1):
        s = ("." * i) + ("*" * sep) + ("." * (n - i))
        print(s)


# draw_shape(6, 3)


def m10(x):
    while x >= 10:
        x -= 10
    return x


def f(x):
    x += 2
    return x**2


x = m10(f(4))
# print(x)


def s(a, b, c, d):
    f1 = a / b
    f2 = c / d
    g = math.gcd(b, d)
    if b == d:
        result = (a + c) / g

    if g == b:
        result = f1 + c / g
    if g == d:
        pass

    result = (a * g) + (c * g)
    return result


def s(lst, val):
    n = []
    for x in lst:
        if x != val:
            n += [x]
    return n


def max_line(lst):
    counter = 0  # length of the values which is not None
    lengths = []
    for line in lst:
        for item in line:
            if item != None:
                counter += 1
        lengths.append(counter)
        counter = 0

    mx = lengths[0]
    for item in lengths[1:]:
        if item > mx:
            mx = item

    return mx


def max_line(lst):
    counter = 0  # length of the values which is not None
    mx = 0
    for line in lst:
        for item in line:
            if item != None:
                counter += 1
        if counter > mx:
            mx = counter
        counter = 0
    return mx


def nbc(x):
    if x == 0:
        return 0
    else:
        print("OK")
        return 1 + nbc(x // 10)


x = nbc(1234)
print(x)
