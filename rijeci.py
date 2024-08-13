from sys import stdin, stdout

map = {}

def build_str(k):
    if k == 0:
        return "A"
    if k == 1:
        return "B"
    elif k in map:
        return map[k]
    val = build_str(k-1) + build_str(k-2)
    map[k] = val
    return map[k]

def rijeci(k):
    string = "A"
    string = build_str(k)
    a_count, b_count = 0, 0
    for c in string:
        if c == "A":
            a_count += 1
        elif c == "B":
            b_count += 1
    return a_count, b_count

k = int(stdin.readline().strip())

a, b = rijeci(k)

stdout.write(f"{a} {b}\n")