#! python3
grid = [[1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
print(*grid, sep='\n')
start = (3, 0)
end = (0, 0)
print("====================")
distance_grid = [[0] * len(grid[0])] * len(grid)
print(*distance_grid, sep='\n')

