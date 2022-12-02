if __name__ == "__main__":

    with open('input/d_02.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    d = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': 0,
        'Y': 1,
        'Z': 2,
    }

    s = 0
    for line in lines:
        a, b = line.split()
        s += d[b] + 1
        s += 3 * ((d[b] - d[a] + 1) % 3)
    print('p1: ', s)

    s = 0
    for line in lines:
        a, b = line.split()
        s += 3 * d[b]
        s += (d[a] + (d[b] - 1)) % 3 + 1
    print('p2: ', s)
