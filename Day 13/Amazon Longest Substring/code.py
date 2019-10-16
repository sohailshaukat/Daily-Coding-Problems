#! python3
import sys

try:
    if sys.argv[1]:
        s = sys.argv[1]
except:
    s = "abcba"
try:
    if sys.argv[2]:
        k = int(sys.argv[2])
except:
    k = 2


def distincter(string, k):
    distinct_char = {}
    s = []
    for char in string:
        try:
            if distinct_char[char]:
                s.append(char)
                continue
        except KeyError:
            if len(distinct_char.keys()) < k:
                s.append(char)
                distinct_char[char] = True
            else:
                break
    return ''.join(s)


arr = []
longest_distinct_string_length = 0

for ptr, char in enumerate(s):
    distinct_string = distincter(s[ptr::], k)
    if len(distinct_string) > longest_distinct_string_length:
        longest_distinct_string_length = len(distinct_string)
        result = distinct_string

print(result)
