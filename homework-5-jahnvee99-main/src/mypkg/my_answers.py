#!/usr/bin/python

"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generate(ans,have,open,close,numPara):
    if open == numPara and close == numPara:
        ans.append(have)
        return
    if open < numPara:
        generate(ans,have+"(",open+1,close,numPara)
    if close < open:
        generate(ans,have+")",open,close+1,numPara)

def generateParenthesis(numPara):
    ans = []
    generate(ans,"",0,0,numPara)
    return ans


assert generateParenthesis(0) == ['']
assert generateParenthesis(1) == ['()']
assert generateParenthesis(2) == ['(())', '()()']
assert generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']




"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""

def isPalindrome(input_str):

    if input_str == "":
        return True
    else :
        input_str = input_str.lower()
        input_str = ''.join(x for x in input_str if x.isalnum())
        reverse_str = input_str[::-1]
        if input_str == reverse_str:
            return True
        else:
            return False

assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False




