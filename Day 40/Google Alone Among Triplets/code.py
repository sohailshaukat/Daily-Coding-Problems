#! python3

arr = [6, 3, 1, 3, 3, 6, 6]

ptr = 0
result = 0
while ptr < len(arr):
    el = arr[ptr]
    anchor = ptr
    try:
        if arr[anchor+1::].index(el):
            pass
    except ValueError:
        try:
            if arr[anchor-1::-1].index(el):
                pass
        except ValueError:
            result = el
            break
    ptr += 1

print(result)
