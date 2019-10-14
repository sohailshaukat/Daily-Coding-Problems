#! python3
class House:

    def __init__(self, color="white", index=0):
        self.color = color
        self.index = index
        self.cost = self.costComputer()

    def costComputer(self):
        if self.color == "white":
            return 0
        else:
            global colors
            color_weight = colors.index(self.color) + 1
            cost = color_weight*self.index
        return cost

    def paint(self, color):
        print(f"Painting House at index {str(index)}")
        self.color = color


colors = ['red', 'brown', 'cyan']
house_row = []
for index in range(0, 7):
    house = House(index=index)
    house_row.append(house)
cost = 0
alternator = not (len(house_row) % 2 == 0)

for index, house in enumerate(house_row):
    if alternator:
        house_row[index].paint(colors[0])
    else:
        house_row[index].paint(colors[1])
    alternator = not alternator
    cost += house.costComputer()
print(cost)
