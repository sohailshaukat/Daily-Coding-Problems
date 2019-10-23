#! python3
class LinkedList:
    last = None

    def __init__(self):
        self.root = Node(0)
        self.last = self.root

    def pushNode(self, node):
        self.last.next = node
        self.last = self.last.next

    def popNode(self):
        current = self.root
        last = self.last
        second_last = None
        if current == last:
            raise Exception("[+]Root node cannot be deleted.")
        while current != last:
            second_last = current
            current = current.next
        popper = self.last
        del self.last
        self.last = second_last
        return popper

    def __repr__(self):
        llist = []
        current = self.root
        while current != self.last:
            llist.append(str(current.info))
            current = current.next
        if current == self.last:
            llist.append(str(current.info))
        return '->'.join(llist)


class Node:

    def __init__(self, info=None, next=None):
        self.next = next
        self.info = info


llist = LinkedList()
for i in range(1, 10):
    llist.pushNode(Node(i))

print(llist)

# ONLY TO ADD A FUNCTION THAT HAS TWO POINTERS WE'LL CALL THEM LEGS ONE WILL BE AHEAD AND ONE WILL BE K STEPS BACK
fptr = llist.root  # Leg that stays k steps ahead of sptr
sptr = llist.root  # Leg that stays k steps behind sptr
step = 0

k = 3              # To get k th last element
print(f"[+]k = {str(k)} \n[+]k th last element is:")
while fptr != llist.last:
    if step >= k:  # Letting fptr lead for k iterations so sptr can lag behind it
        sptr = sptr.next
    fptr = fptr.next
    step += 1

sptr = sptr.next
print("...\t\t\t",sptr.info)
