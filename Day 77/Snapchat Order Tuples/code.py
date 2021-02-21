# ! python3


def binaryInsert(arr, element):
    depletion_arr = arr
    dep_arr_length = len(depletion_arr)
    distance = dep_arr_length//2
    if dep_arr_length == 0:
        return [element]
    elif dep_arr_length == 1:



arr = [(1, 3), (5, 8), (4, 10), (20, 25)]
sorted_arr = []
min_arr = []
tuple_dict = {}
curr_max = -99999

for tup in arr:
    curr_min = min(tup)
    tuple_dict[curr_min] = tup
    min_arr = binaryInsert(min_arr, curr_min)

for element in min_arr:
    if element > curr_max:
        sorted_arr.append(tuple_dict[element])
        curr_max = max(tuple_dict[element])
print(sorted_arr)
print(min_arr)