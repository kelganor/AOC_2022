from collections import Counter


def solve(lines, t):
    buffer = dict(Counter(lines[:t]))
    s = len(buffer.values())
    prev = lines[0]
    for i, x in enumerate((lines[t:])):
        if s == t:
            return i + t
        buffer[prev] -= 1
        if buffer[prev] == 0: s -= 1
        buffer[x] = buffer.get(x, 0) + 1
        if buffer[x] == 1: s += 1
        prev = lines[i+1]

    return -1


with open('input/d_06.txt') as f:
    lines = f.read()
print(solve(lines, 4))
print(solve(lines, 14))
