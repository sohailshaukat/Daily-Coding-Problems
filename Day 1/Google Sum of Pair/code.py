#! python3
'''
Input: 
    k = 17
    array = 10 15 3 7
Output: True

p.s: Use commmand line arguments to pass arguments.
For Eg Case 1:
    python code.py "17" "10 15 3 7"
'''
import sys

k = int(sys.argv[1])
arr = sys.argv[2].split()
arr = [int(num) for num in arr]
compliment_map = {}
ptr = 0
presence = False
while ptr < len(arr):
    try:
        if compliment_map[k-arr[ptr]]:        
            presence = True
    except:
        compliment_map[arr[ptr]] = True
    ptr += 1
print(presence)