from sys import stdin, stdout

def rijeci(k):
    string = "A"
    for _ in range(k):
        a_count, b_count = 0, 0
        arr = []
        for _, c in enumerate(string):
            if c == "A":
                arr.append("B")
                b_count += 1
            elif c == "B":
                arr.append("BA")
                b_count += 1
                a_count += 1

        string = "".join(arr)
    return a_count, b_count

k = int(stdin.readline().strip())

a,b = rijeci(k)

stdout.write(f"{a} {b}\n")