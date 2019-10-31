#! python3


def findSecondLargest(root):
    largest = 0
    secondLargest = 0
    stack = [root]
    ptr = 0
    while ptr < len(stack):
        if stack[ptr].left != None:
            stack.append(stack[ptr].left)
        if stack[ptr].right != None:
            stack.append(stack[ptr].right)
        if stack[ptr].info > largest:
            secondLargest = largest
            largest = stack[ptr].info
        elif stack[ptr].info > secondLargest:
            secondLargest = stack[ptr].info
        ptr += 1
