#! python3

string = "AAAABBBCCDAA"

ptr = 0

rle = []
while ptr < len(string):
    if rle == []:
        rle.append([string[ptr], 1])
    elif string[ptr] == rle[-1][0]:
        rle[-1][1] += 1
    else:
        rle.append([string[ptr], 1])
    ptr += 1

for ptr, pair in enumerate(rle):
    rle[ptr][1] = str(pair[1])
    rle[ptr] = ''.join(pair[::-1])

print("[+] Original String: "+string)
print("[+] RLEncoded String: "+''.join(rle))
