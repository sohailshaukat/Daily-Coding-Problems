import random


class Element:

    def __init__(self,  id, picked=False):
        self.id = id
        self.picked = picked


class ElementMemory:

    def __init__(self):
        self.view = []
        self.pickerCount = 0
        self.size = 0

    def addElement(self, element_id):
        self.view.append(Element(id=element_id))
        self.size += 1

    def pickFlush(self):
        for element in self.view:
            element.picked = False

    def pickRandomElement(self):
        if self.pickerCount == self.size:
            self.pickerCount = 0
            self.pickFlush()
        while True:
            index = random.randrange(len(self.view))
            element = self.view[index]
            if element.picked == False:
                self.pickerCount += 1
                element.picked = True
                return element.id

    def display(self):
        for element in self.view:
            print(element.id)


memory = ElementMemory()

memory.addElement("element#1")
memory.addElement("element#2")
memory.addElement("element#3")
memory.addElement("element#4")
memory.addElement("element#5")

memory.display()

##### Tests #####
print("################")
print(memory.pickRandomElement())
print(memory.pickRandomElement())
print(memory.pickRandomElement())
print(memory.pickRandomElement())
print(memory.pickRandomElement())

print(memory.pickRandomElement())
print(memory.pickRandomElement())
print(memory.pickRandomElement())
print(memory.pickRandomElement())
print(memory.pickRandomElement())
