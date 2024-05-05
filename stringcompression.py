from typing import List


def compress(chars: List[str]) -> int:
    s = ""
    count = 1
    char = chars[0]
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
            char = chars[i]
        else:
            s += char
            char = chars[i]
            if count > 1:
                s += str(count)
            count = 1

    s += char
    if count > 1:
        s += str(count)
    for i, c in enumerate(s):
        chars[i] = c

    print(s)
    return len(s)


compress(["a","b", "c"])
compress(["a"])