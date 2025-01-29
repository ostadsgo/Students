def insert_middle(lst, x):
    if lst == []:
        return [x]

    middle = len(lst) // 2
    # insert middle in middle of the lst
    result = lst[:middle] + [x] + lst[middle:]
    return result


def extract_multiples(pairs):
    results = []
    for pair in pairs:
        if pair[0] % pair[1] == 0:
            results.append(pair)
    return results


def extract_multiples(pairs):
    results = []
    for pair in pairs:
        number, divisor = pair
        if number % divisor == 0:
            results.append(pair)
    return results


def sum_of_pos(lst):
    total = 0
    for numbers in lst:
        for number in numbers:
            if number > 0:
                total += number
    return total


def smooth_list(lst):
    result = []

    if lst == []:
        return result

    result.append(lst[0])

    for i in range(1, len(lst)):
        r = (lst[i] + lst[i - 1]) / 2
        result.append(r)

    return result


def myabs(x):
    if x >= 0:
        return x
    return x + 2 * -x


def myabs_list(lst):
    result = []
    for item in lst:
        result.append(myabs(item))
    return result


def equal_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False

    return True


def equal_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    for a, b in zip(lst1, lst2):
        if a != b:
            return False

    return True


def is_pos_list(lst):
    str_lst = []
    for item in lst:
        str_lst.append(str(item))

    for item in str_lst:
        if "-" in item:
            return False
    return True


def mirror_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])

    return result


def mirror_list(lst):
    return lst[::-1]


def mirror_list(lst):
    result = [0] * len(lst)
    i = len(lst) - 1
    for item in lst:
        result[i] = item
        i -= 1
    return result


def is_mirror_whatever_sign(lst1, lst2):
    if lst2 == lst1[::-1]:
        return True

    abs_list1 = myabs_list(lst1)
    abs_list2 = myabs_list(lst2)
    if abs_list1[::-1] == abs_list2:
        return True

    return False


print(is_mirror_whatever_sign([1, 2, 3, 4], [1, 2, 3, 4]))
print(is_mirror_whatever_sign([1, 2, 3, 4], [4, 3, 2, 1]))
print(is_mirror_whatever_sign([1, -2, 3, -4], [4, -3, 2, 1]))
