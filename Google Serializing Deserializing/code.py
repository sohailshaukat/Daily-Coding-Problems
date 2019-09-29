#! python3
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    node_stack = [node]
    sptr = 0
    while sptr != len(node_stack):
        if node_stack[sptr]:
            if node_stack[sptr].left:
                node_stack.append(node_stack[sptr].left)
            else:
                node_stack.append(None)
            if node_stack[sptr].right:
                node_stack.append(node_stack[sptr].right)
            else:
                node_stack.append(None)
        sptr += 1
    val_stack = []
    for node in node_stack:
        if node:
            val_stack.append(node.val)
        else:
            val_stack.append("-1")
    return " ".join(val_stack)


def deserialize(tree):
    val_stack = tree.split()
    node_stack = []
    for val in val_stack:
        if val != "None":
            node_stack.append(Node(val))
        else:
            node_stack.append(None)
    sptr = 0
    fptr = 1
    while fptr != len(node_stack):
        node_stack[sptr].left = node_stack[fptr]
        fptr += 1
        node_stack[sptr].right = node_stack[fptr]
        fptr += 1
        sptr += 1
    return node_stack[0]


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print((deserialize(serialize(node))).left.left.val)
