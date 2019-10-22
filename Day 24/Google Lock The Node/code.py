#! python3
class BinaryTree:

    def __init__(self, parent=False, left=None, right=None, locked_status=False):
        self.root = Node(info="root", parent=parent, left=left,
                         right=right, locked_staus=locked_status)


class Node:

    def __init__(self, info, parent=None, left=None, right=None, locked_status=False):
        self.info = info
        self.parent = parent
        self.left = left
        self.right = right
        self.locked_status = locked_status

    def is_locked(self):
        return self.locked_status

    def lock(self):
        if checkAncestorStatus(self) or checkDescendantStatus(self):
            return False
        else:
            self.locked_status = True

    def unlock(self):
        if checkAncestorStatus(self) or checkDescendantStatus(self):
            return False
        else:
            self.locked_status = False


def checkAncestorStatus(node):
    current = node.parent
    while current.parent:
        if current.locked_status:
            return True
        current = current.parent
        if current.parent == None:
            if current.locked_status:
                return True
    return False


def checkDescendantStatus(node):
    if node:
        checkDescendantStatus(node.left)
        if node.locked_status:
            return False
        checkDescendantStatus(node.right)
