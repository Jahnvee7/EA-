#!/usr/bin/python

"""
Python Core object Types
"""


def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Write the value 4 to the pwor of 5
    x = 4**5

    # Assign a string "Stevens" to a variable y
    y = "Stevens"

    # Repeat variable y 7 times
    z = y*7

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is Great"
    m = y + " is Great"

    # Replace "Great" with "Good" in variable m and assign it to a new variable n
    n = m.replace("Great","Good")

    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Hoboken is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(" ")

    # Get all the items past the first of the third substring
    r = p[2][1:]

    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    A = [[1,4,5],[6,10,11],[12,17,38]]

    # Collect the items in the last column of matrix A using list comprehension
    c = [x[2] for x in A]

    # Collect only the even items of the diagonal of matrix A using list comprehension
    d = [A[i][i] for i in [0,1,2] if A[i][i] % 2 == 0]

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    j = "Stevens"
    o =  [ord(x) for x in j]

    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 18
    #   color => "red"
    f = {"fruit":"apple","quantity":18,"color":"red"}

    # Get the item in dictionary f that the key "fruit" maps to
    a = f["fruit"]
    # Increase the quantity of f by 1
    f["quantity"]+= 1

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    amazing_grace = { "name":{"first_name":"Grace", "last_name":"Hopper"}, "jobs":["scientist", "engineer"], "age":85}

    # Add "programmer" to the list of jobs Grace has
    amazing_grace["jobs"].append("programmer")

    # Get the third job Grace has that you recently added
    p = amazing_grace["jobs"][2]

    # Get the sorted keys of amazing_grace in alphabetically ascending order
    k = list(amazing_grace.keys())
    k.sort(reverse=False)

    return a, f, p, k


numbers_and_strings()
lists()
dictionaries()
