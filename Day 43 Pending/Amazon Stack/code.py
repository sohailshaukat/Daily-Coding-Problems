#! python3

import multiprocessing


class Stack:

    occCache = {}
    stack = []
    currentMax = None
    # def __init__(self):
    #     pass

    def __repr__(self):
        return " ".join(self.stack)

    # def binaryInsert(self, val):
    #     tempList = self.sortedList
    #     distance = len(tempList)//2
    #     if self.sortedList == []:
    #         self.sortedList.append(val)
    #     else:
    #         while len(tempList) != 1:
    #             if val > tempList[len(tempList)//2]:
    #                 tempList = tempList[len(tempList)//2::]
    #                 distance += len(tempList)//2
    #             else:
    #                 tempList = tempList[:len(tempList)//2:]
    #                 distance -= len(tempList)//2
    #         if tempList[0] > val:
    #             self.sortedList.insert(distance-1, val)
    #         else:
    #             self.sortedList.insert(distance+1, val)

    def pop(self):
        # return stack.pop()
        try:
            val = self.stack[-1]
            self.occCache[val] -= 1
            del self.stack[-1]
        except:
            print("[-] Stack is empty.")
            val = None
        return val

    def push(self, val):
        if val > self.currentMax:
            self.currentMax = val
        try :
            self.occCache[val] += 1
        except KeyError:
            self.occCache[val] = 1
        self.stack.append(str(val))

    def max(self):
        if self.stack == []:
            print("[-] Stack is empty.")
            return
        else:
            return max(stack)


stack = Stack()
stack.push(4)
stack

print(stack)
