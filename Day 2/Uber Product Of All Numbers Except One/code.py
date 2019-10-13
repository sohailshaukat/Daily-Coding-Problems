#! python3
'''
Case 1:
    Input: 1 2 3 4 5 
    Output: 120 60 40 30 24
Case 2:
    Input: 3 2 1
    Output: 2 3 6
p.s: Use commmand line arguments to pass arguments.
For Eg Case 1:
    python code.py "1 2 3 4 5"
'''
import sys

left_cache = []
right_cache = []
new_arr = []
arr = sys.argv[1].split()
left_cache.append(int(arr[0]))
right_cache.append(int(arr[-1]))
for ptr,num in enumerate(arr[1::]) :
    left_cache.append(left_cache[ptr]*int(num))
for ptr,num in enumerate(arr[-2::-1]):
    right_cache.insert(0,right_cache[0]*int(num))
new_arr.append(right_cache[1])
new_arr.append(left_cache[-2])
for ptr,num in enumerate(arr[1:-1]):
    new_arr.insert(ptr+1, left_cache[ptr]*right_cache[ptr+2])
print(new_arr)