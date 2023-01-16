#!/usr/bin/python

"""
Python  Functions
"""


# Write a Python function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)

def unique_list(un_li):
    x = []
    for i in range(len(un_li)):
        if un_li[i] not in x:
            x.append(un_li[i])
    return x


# Write a Python function multiply()to multiply all giving numbers in a list.
# Sample List : (9, 2, 3, -6, 7)
# Expected Output : -2268


def multiply(mul_li):
    total = 1
    for i in range(len(mul_li)):
        total *= mul_li[i]
    return total


# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12

def get_average(*avg):
    num = 0
    for i in range(len(avg)):
        num += avg[i]
    num = num / len(avg)
    return num / count


assert get_average(5,6,8,10,31) == 12
assert multiply([9, 2, 3, -6, 7]) == -2268
assert unique_list([1,2,3,3,3,3,4,4,5]) == [1, 2, 3, 4, 5]