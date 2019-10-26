#! python3

grid = [[1, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]

for i, frame in enumerate(grid):
    for j, tile in enumerate(frame):
        if tile == 1:
            grid[i][j] = False
        else:
            grid[i][j] = True

start = (3, 0)
start_i, start_j = start
end = (0, 0)
end_i, end_j = end

i, j = start

grid[start_i][start_j] = 0

stack = [start]
print("[+] M x N Matrix where True represents Wall and False represents tile:\n")
print(*grid, sep='\n')
print("\n\n")
ptr = 0
while (i, j) != end:
    try:
        if grid[i+1][j] == False:
            grid[i+1][j] = grid[i][j] + 1
            print(grid[i][j] + 1)
            stack.append((i+1, j))
    except:
        pass
    try:
        if grid[i-1][j] == False:
            grid[i-1][j] = grid[i][j] + 1
            stack.append((i-1, j))
    except:
        pass
    try:
        if grid[i][j+1] == False:
            grid[i][j+1] = grid[i][j] + 1
            stack.append((i, j+1))
    except:
        pass
    try:
        if grid[i][j-1] == False:
            grid[i][j-1] = grid[i][j] + 1
            stack.append((i, j-1))
    except:
        pass
    if (i, j) == start:
        grid[i][j] = 1
    ptr += 1
    i, j = stack[ptr]

print("[...] Calculating distance for each tile...\n")
print(*grid, sep='\n')
print("\n\n")
print(
    f"[+] Shortest distance from {start_i},{start_j} to {end_i},{end_j} is {grid[end_i][end_j]} tiles")
