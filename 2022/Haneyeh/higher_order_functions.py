# v1
def select_divided_by_3_or_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
    
# v2
def select_divided_by_3_or_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False

# v3: if expression
def select_divided_by_3_or_5(n):
    return True if n % 3 == 0 or n % 5 == 0 else False

# v4: if expression
def select_divided_by_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0




def is_divided_by_3_or_5(numbers):
    result = []
    for n in numbers:
        if n % 3 == 0 or n % 5 == 0:
            result.append(n)

    return result


def is_divided_by_3_or_5(numbers):
    return list(filter(select_divided_by_3_or_5, numbers))

def is_divided_by_3_or_5(numbers):
    return list(filter(lambda n: n % 3 == 0 or n % 5 == 0, numbers))


x = is_divided_by_3_or_5([1, 9, 8, 10, 12, 13, 11, 15, 18, 20])
print(x)
