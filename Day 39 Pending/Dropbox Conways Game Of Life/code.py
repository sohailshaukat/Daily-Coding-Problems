#! python3
class Grid:

    baseGrid = []

    def __init__(self, topMost):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


class Cell:

    def __init__(self, pos, isAlive):
        self.pos = pos
        self.isAlive = isAlive


def should_i_be_dead(cell):
    neighbours = []
