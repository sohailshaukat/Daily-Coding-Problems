#! python3

arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
count_dict = {'R': 0, 'G': 0, 'B': 0}
ptr = 0
while ptr < len(arr):
    char = arr[ptr]
    if char == 'R':
        arr.insert(0, 'R')
    elif char == 'G':
        arr.insert(count_dict['R'], 'G')
    elif char == 'B':
        arr.insert(count_dict['R'] + count_dict['G'], 'B')
    count_dict[char] += 1
    del arr[ptr+1]
    ptr += 1
print(arr)
