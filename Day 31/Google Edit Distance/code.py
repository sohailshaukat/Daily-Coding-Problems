#! python3
def countCommon(string_1, string_2):
    count = 0
    for ptr, char in enumerate(string_1):
        if string_2[ptr] == char:
            count += 1
    return count


string_1 = "kitten"
string_2 = "sitting"
if len(string_1) < len(string_2):
    substring = string_1
    superstring = string_2
elif len(string_1) > len(string_2):
    substring = string_2
    superstring = string_1


head = 0
tail = len(substring)
closest_match_index = 0
maximum_common = 0
while tail < len(superstring):
    comm_count = countCommon(substring, superstring[head: tail])
    if comm_count > maximum_common:
        maximum_common = countCommon
        closest_match_index = head
    head += 1
    tail += 1

# Deletion
difference = len(superstring) - len(substring)
superstring = superstring[closest_match_index: len(substring)]

# Substitution
substitutions = len(superstring) - countCommon(superstring, substring)

print(
    f"[+] Edit Distance between {string_1} and {string_2} is {difference + substitutions}")
