### [input - data]
##number1 = input("Enter a number: ")
##number2 = input("Enter another number: ")
##
### Process - operation
##total = int(number1) + int(number2)
##
### [output]
##print("Total is", total)


# 2
### -----------------
##n = input("Enter a number: ")
##res = int(n) ** 2
##print("Result is:", res)

import math
# 3
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

delta = b ** 2 - 4 * a * c
print("Delta: ", delta)

if delta > 0:
    p_x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    n_x = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("Positive root is", p_x)
    print("Negative root is", n_x)
elif delta < 0:
    print("Delta is negative so there is no answer")
else:
    print(detal)


