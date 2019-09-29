#! python3
'''
Case 1:
    Input: 3 4 -1 -1
    Output: 2
Case 2:
    Input: 1 2 0
    Output: 3
p.s: Use commmand line arguments to pass arguments.
For Eg Case 1:
    python code.py "3 4 -1 -1"
'''
import sys


arr = sys.argv[1].split()
arr = [int(num) for num in arr]
maximum = 0
minimum = 99999999999999
for num in arr:
    if num > maximum:
        maximum: maximum = num
    if num < minimum and num > 0:
        minimum = num
if minimum == 1:
    print(maximum+1)
else:
    print(minimum-1)
