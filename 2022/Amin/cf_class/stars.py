
# function defination
##def star(star_length):
##    shape = "*"
##
##    # accuemlator
##    result = ""
##    for x in range(star_length):
##        result = result + shape
##        
##    print(result)


def star_2(length):
    return '*' * length


def starbandwidth(l, left, space):
    shape = '*'
    return shape * left + space * ' ' + (l - (left+space)) * shape

def display_triangle(w, sn):
    """
    w: int -> width of the triangle a single line.
    sn: int -> number of space
    """
    l = w - sn + 1   # length (hight)
    
    
    #line = ' ' * sn + '*' * (w - sn)
    for i in range(l):
        line = '*' * i + ' ' * sn + '*' * (w - sn - i)
        print(line)


def sum_lst(lst):
    total = 0
    for element in lst:
        total += element   # total = total + element
        
    return total

def sum_lst_x(lst):
    total = 0
    for index in range(len(lst)):
        number = lst[index]
        total += number
    return total


def sum_lst(lst):
    a1 = lst[0]
    an = lst[-1]
    sn = len(lst) * ((a1 + an) / 2)
    return sn


def normalize(lst):
    total = sum_lst(lst)
    result_lst = []
    for elm in lst:
        result_lst.append(elm / total)

    rst = sum_lst(result_lst)
    return rst
        
    
from random import randint


for j in range(100):
    nums = []
    for i in range(10):
        rnum = randint(1, 100)
        nums.append(rnum)

    
    
    n = normalize(nums)
    if n != 1.0:
        print(nums, n)
        

