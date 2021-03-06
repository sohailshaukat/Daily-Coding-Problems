#! python3

grid = [[0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 1, 0]]


class Path:
    def __init__(self, anchor, direction, length):
        self.anchor = anchor  # (i,j)
        # True for Up , False for Left
        self.direction = direction
        self.length = length

    def maximumPathFinder(grid, anchor):
        path_up = Path.upPathCalculator(grid, anchor)
        path_left = Path.leftPathCalculator(grid, anchor)
        if path_up.length > path_left.length:
            return path_up
        else:
            return path_left

    def upPathCalculator(grid, anchor):
        i, j = anchor
        length = 0
        while grid[i][j] == 1 and i > -1:
            length += 1
            i -= 1
            try:
                if not grid[i][j]:
                    break
            except:
                break
        return Path(anchor, True, length)

    def leftPathCalculator(grid, anchor):
        i, j = anchor
        length = 0
        while grid[i][j] == 1 and j > -1:
            length += 1
            j -= 1
            try:
                if grid[i][j]:
                    pass
            except:
                break
        return Path(anchor, False, length)

    def pathPainter(self, grid):
        grid = [['W' for el in (grid[0])] for row in grid]
        i, j = self.anchor
        length = self.length
        if self.direction:
            while length:
                grid[i][j] = 'L'
                i -= 1
                length -= 1
        else:
            while length:
                grid[i][j] = 'L'
                j -= 1
                length -= 1
        return grid


paths = []
for i, row in enumerate(grid):
    for j, spot in enumerate(row):
        if spot == 1:
            path = Path.maximumPathFinder(grid=grid, anchor=(i, j))
            paths.append(path)
maximum_runway_length = 0
maximum_runway_path = None
for path in paths:
    if path.length > maximum_runway_length:
        maximum_runway_length = path.length
        maximum_runway_path = path
grid = maximum_runway_path.pathPainter(grid)
print(*grid, sep='\n')
