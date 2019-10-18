#! python3
UNIVERSAL_TREES_COUNT = 0


def inOrder(root):
    # Write your code here
    global UNIVERSAL_TREES_COUNT
    if root:
        if root.left.info == root.right.info:
            UNIVERSAL_TREES_COUNT += 1
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
