#! python3


def binaryInsertion(arr, element):
    depletion_arr = arr
    distance = len(depletion_arr)//2
    while len(depletion_arr) != 1:
        if element > depletion_arr[len(depletion_arr)//2]:
            depletion_arr = depletion_arr[len(depletion_arr)//2::]
            distance += len(depletion_arr)//2
        else:
            depletion_arr = depletion_arr[:len(depletion_arr)//2:]
            distance -= len(depletion_arr)//2
    if depletion_arr[0] > element:
        arr.insert(distance-1, element)
    else:
        arr.insert(distance+1, element)
    return arr


data = [2, 1, 5, 7, 2, 0, 5]
memory = [data[0]]
ptr = 1
print(memory[0])
while ptr < len(data):
    memory = binaryInsertion(memory, data[ptr])
    if len(memory) % 2 != 0:
        print(memory[len(memory)//2])
    else:
        median = (memory[len(memory)//2] + memory[len(memory)//2-1])/2
        print(median)
    ptr += 1
