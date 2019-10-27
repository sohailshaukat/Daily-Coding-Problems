#! python3


def get_capacity(peaks):
    print("[+] Peaks or Building Heights :")
    print(*peaks, sep="|")
    depth = 0
    capacity = 0
    brim = peaks[0]
    for ptr, height in enumerate(peaks):
        if brim > height:
            depth += (brim-height)
        else:
            brim = height
            capacity += depth
            depth = 0
    return "[+] Capacity of the valley is :\t"+str(capacity)+"\n"


print("[...] ...")
print(get_capacity([3, 0, 1, 3, 0, 5]))
print(get_capacity([2, 1, 2]))
