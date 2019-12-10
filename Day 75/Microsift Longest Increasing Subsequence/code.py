#!python3
import sys

try:
    arr = [int(num) for num in sys.argv[1].split()]
except:
    arr_choice = input("[*] Any key for Default Array, N for Custom: \n")
    if arr_choice.lower() != 'n':
        arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    else:
        arr = [int(num) for num in input().split()]

print("[+]Array: ", arr)

arr_length = len(arr)

length_cache = [1]*arr_length
subsequence_index = [0]*arr_length
maximum_length = 1
anchor = 0
subsequence = ["0"]
sptr = 0
fptr = 1

while fptr < arr_length:
    while sptr < fptr:
        if arr[sptr] < arr[fptr] and length_cache[sptr] >= length_cache[fptr]-1:
            length_cache[fptr] = length_cache[sptr] + 1
            subsequence_index[fptr] = sptr
            if length_cache[fptr] > maximum_length:
                maximum_length = length_cache[fptr]
                anchor = fptr
        sptr += 1
    sptr = 0
    fptr += 1

print("[+] Length of the longest subsequence: ", maximum_length)

while anchor != 0:
    subsequence.insert(1, str(arr[anchor]))
    anchor = subsequence_index[anchor]

print("[+] Subsequence: "+'->'.join(subsequence))
