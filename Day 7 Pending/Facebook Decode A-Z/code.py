#! python3

class Node:

    def __init__(self, left = None, right = None, parent = None, info = None, remaining = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.info = info
        self.remaining = remaining
root = Node(info="$")

string = "111"

stack = [root]
ptr = 0
while ptr < len(string):
    current = stack[ptr]
    current.left = Node(info = string[ptr], remaining= string[ptr+1::], parent = current)
    stack.append(current.left)
    if int(string[ptr:ptr+2:]) <= 26:
        current.right = Node(info = string[ptr:ptr+2], remaining= string[ptr+2::], parent = current)
        stack.append = current.right
    ptr += 1