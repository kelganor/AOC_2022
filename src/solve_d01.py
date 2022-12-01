if __name__ == "__main__":

    with open('input/d_01.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    g = []
    cur = 0
    for x in lines:
        if x == '':
            g.append(cur)
            cur = 0
        else:
            cur += int(x)

    print('p1: ', max(g))

    g = sorted(g)
    print('p2: ', sum(g[-3:]))
