# ! python3


arr = [(1, 3), (5, 8), (4, 10), (20, 25)]

minimum = 999
maximum = 0

for tup in arr:
    curr_min = min(tup)
    curr_max = max(tup)
    if curr_min < minimum:
        minimum = curr_min
        