from sys import stdin, stdout

seq = {}

def build_str(k):
    if k == 0:
        # return "A"
        return 1, 0
    if k == 1:
        # return "B"
        return 0, 1
    elif k in seq:
        return seq[k]
    val = tuple(map(sum, zip(build_str(k-1), build_str(k-2))))
    # print(val)
    seq[k] = val
    return seq[k]

def rijeci(k):
    a, b = build_str(k)
    return a, b

k = int(stdin.readline().strip())

a, b = rijeci(k)

stdout.write(f"{a} {b}\n")