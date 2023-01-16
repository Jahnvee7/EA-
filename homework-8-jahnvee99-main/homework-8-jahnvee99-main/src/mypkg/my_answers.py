# !/usr/bin/python

"""
Linked Lists, Stacks and Queues
"""

"""
QUESTION 1: 
========================================================================================================
Write a Python function to implement a recursive algorithm which counts the number of nodes in a 
singly linked list. The input of the function should be a reference pointing to the first node of the
linked list. The output of the function should be the number of nodes in that linked list. 
Your function should be robust enough to handle possible inappropriate inputs.
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
Outpot :  5
"""


class Node(object):
    def __init__(self, value=None, next_node=None):
        self.data = value
        self.next = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


def countNodes(self):
    return countNodes(self.next) + 1 if self else 0



"""
QUESTION 2: 
========================================================================================================
Write a function evalPostfix that takes a string with space as delimiter and evaluates the value of postfix. Assume we have only two operators: * and +.
	
Evaluate the value for "55 44 + 3 *"
Outpot : 297 


===========================
"""


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0


def evalPostfix(expr):
    tokens = expr.split(" ")
    stack = Stack()
    for token in tokens:
        if token == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            res = num1 + num2
            stack.push(res)
        elif token == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            res = num1 * num2
            stack.push(res)
        else:
            stack.push(int(token))
    return stack.pop()


