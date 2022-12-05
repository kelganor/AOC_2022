if __name__ == "__main__":

    with open('input/d_04.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    res = 0
    for line in lines:
        xa, xb, ya, yb = list(map(int, line.replace('-', ',').split(',')))
        if xa <= ya <= yb <= xb or ya <= xa <= xb <= yb:
            res += 1
    print('p1: ', res)

    res = 0
    for line in lines:
        xa, xb, ya, yb = list(map(int, line.replace('-', ',').split(',')))
        if (xa <= ya <= xb or xa <= yb <= xb or
            ya <= xb <= yb or ya <= xa <= yb):
            res += 1
    print('p2: ', res)
