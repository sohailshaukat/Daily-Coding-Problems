#! python3
arr = [1, 2, 3]

stack = [{}]
ptr = 0
while ptr < len(stack):
    parent = stack[ptr]
    for elem in arr:
        temp = list(parent)
        temp.append(elem)
        if set(temp) not in stack:
            stack.append(set(temp))
    ptr += 1

print(stack)
