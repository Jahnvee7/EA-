#!/usr/bin/python

"""
Python Statements
"""


def add_binary(a, b):
    """
        This is to review binary operations
        ============================================================
        Given two binary strings, return their sum (also a binary string).
        Return None if one of the input strings are empty or contains characters different than 1 or 0.
        Example 1:
                    Input: a = "11", b = "1"
                    Output: result = "100"
        Example 2:
                    Input: a = "1010", b = "1011"
                    Output: result = "10101"
        """
    if a != "" and b != "":
        a_len = len(a)
        b_len = len(b)
        for i in range(0,a_len):
            if a[i] != "0" and a[i] != "1":
                return None
        for i in range(0,b_len):
            if b[i] != "0" and b[i] != "1":
                return None
        carry = 0
        result = ""
        a_len -= 1
        b_len -= 1
        while a_len >= 0 and b_len >= 0:
            sum = int(int(a[a_len]) + int(b[b_len]) + carry)
            carry = int(sum/2)
            sum %= 2
            result = str(sum) + result
            a_len -= 1
            b_len -= 1
        while a_len >= 0:
            sum = int(int(a[a_len]) + carry)
            carry = int(sum/2)
            sum %= 2
            result = str(sum) + result
            a_len -= 1
        while b_len >= 0:
            sum = int(int(b[b_len]) + carry)
            carry = int(sum / 2)
            sum %= 2
            result = str(sum) + result
            b_len -= 1
        if carry > 0:
            result = str(carry) + result
        print(result)
        return result

    else:
        return None

def plus_one(digits):
    """
    This is to review loops and if statements
    ============================================================
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    You can do this in-place!
    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.
    Example 1:
            Input: digits = [1, 2, 3]
            Output: digits = [1, 2, 4]
            Explanation: The array represents the integer 123.
    Example 2:
            Input: digits = [1, 0, 9, 9]
            Output: digits = [1, 1, 0, 0]
    """
    length = len(digits)
    length -= 1
    digits[length] = int(digits[length]) + 1
    extra = int(digits[length]) / 10
    digits[length] %= 10
    i = length - 1
    while i >= 0:
        if extra == 1:
            digits[i] += 1
            extra = digits[i]/10
            digits[i] %= 10
        i -= 1
    if extra == 1:
        digits.insert(0,1)

    print(digits)
    return digits

def roman_to_integers(roman_string):

    """
    This is to review loops, if statements and dictionaries
    ============================================================
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
    Example 1:
        Input: "III"
        Output: 3
    Example 2:
        Input: "IV"
        Output: 4
    Example 3:
        Input: "IX"
        Output: 9
    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.
    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    extra = 0
    i = len(roman_string) - 1
    while i >= 0:
        if Roman_number[roman_string[i]] >= extra:
            integer += Roman_number[roman_string[i]]
        else :
            integer -= Roman_number[roman_string[i]]
        extra = Roman_number[roman_string[i]]
        i -= 1
    print(integer)
    return integer



result = add_binary('', '')
assert (result == None)
result = add_binary('', '1010')
assert (result == None)
result = add_binary('1010', '')
assert (result == None)
result = add_binary('1301', '1010')
assert (result == None)
result = add_binary('1010', '1301')
assert (result == None)
result = add_binary('11', '1')
assert (result == "100")
result = add_binary('1010', '1011')
assert (result == "10101")
result = add_binary('10101111', '010101')
assert (result == '11000100')
result = add_binary('111', '101')
assert(result=='1100')

digits = [1, 2, 3]
assert([1, 2, 4] == plus_one(digits))
digits = [1, 0, 9, 9]
assert([1, 1, 0, 0] == plus_one(digits))
digits = [9, 9]
assert([1, 0, 0] == plus_one(digits))
digits = [1, 9, 9]
assert([2, 0, 0] == plus_one(digits))
digits = [9]
assert([1, 0] == plus_one(digits))


roman_string = "III"
assert(3 == roman_to_integers(roman_string))
roman_string = "IV"
assert (4 == roman_to_integers(roman_string))
roman_string = "IX"
assert (9 == roman_to_integers(roman_string))
roman_string = "LVIII"
assert (58 == roman_to_integers(roman_string))
roman_string = "MCMXCIV"
assert (1994 == roman_to_integers(roman_string))
roman_string = "XC"
assert (90 == roman_to_integers(roman_string))
roman_string = "LXXX"
assert (80 == roman_to_integers(roman_string))
roman_string = "LXXX"
assert (80 == roman_to_integers(roman_string))
roman_string = "CXXXVII"
assert (137 == roman_to_integers(roman_string))