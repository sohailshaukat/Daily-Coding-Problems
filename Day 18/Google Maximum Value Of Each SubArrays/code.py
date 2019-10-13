#! python3

arr = [10, 5, 2, 7, 8, 7]
k = 3
ptr = 0
while ptr < len(arr):
    if ptr < len(arr)-3:
        arr[ptr]= max(arr[ptr:ptr+3:1])
    else:
        del arr[ptr]
    ptr += 1
print(arr)