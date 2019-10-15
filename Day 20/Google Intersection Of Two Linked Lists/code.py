#! python3
def findMergeNode(head1, head2):
    current = head1
    stack = []
    while current:
        stack.append(current)
        current = current.next
    current = head2
    while current:
        if current.next in stack:
            return current.next.data
        current = current.next
    return
