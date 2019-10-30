#! python3


def isSemiPalindrome(superstring, substring):
    if len(substring) > len(superstring)//2:
        return False
    substring = substring[::-1]
    ptr = 0
    offset = len(substring)
    while ptr < len(substring):
        if substring[ptr] != superstring[offset + ptr]:
            return False
        ptr += 1
    return True


def completeMe(string):
    ptr = 0
    flag = True
    while ptr < len(string):
        if isSemiPalindrome(string, string[:ptr+1]):
            remainder = string[ptr::]
            remainder_arr = [char for char in remainder[::-1]]
            remainder_arr.extend(string)
            flag = False
            break
        ptr += 1
    if flag:
        remainder = string[1::]
        remainder_arr = [char for char in remainder[::-1]]
        remainder_arr.extend(string)
    return (''.join(remainder_arr))


print("[+]For the word 'google' :")
print("\t\t\t"+completeMe('google')+"\n")
print("[+]For the word 'race' :")
print("\t\t\t"+completeMe('race')+"\n")
