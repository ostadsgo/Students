def ceer_normal(lst):
    total = 0
    for item in lst:
        total += item

    result = []
    for item in lst:
        x = item / total
        result.append(x)

    return result


def sum_of_prev_items(lst):
    t = 0
    result = []
    for item in lst:
        t = t + item
        result.append(t)
    return result


def inserter(lst, value, index):
    return lst[:index] + [value] + lst[index:]


def index_inc(lst, val):
    index = 0
    for item in lst:
        # 1. if val exist in lst
        if item == val:
            return index

        # 2. val less than first element of greather than itself.
        if val < item:
            return index

        index += 1

    return index


def insertation_sort(lst):
    sorted_list = []
    for j in range(len(lst)):
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                sorted_list.append(lst[i])
                sorted_list.append(lst[i - 1])

    return sorted_list


def sum_div23(n):
    t = 0
    for i in range(1, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            t += i
    return t


def sum_div23(n):
    if n == 1:
        return
    return sum_div23(n - 1)
