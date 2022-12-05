from collections import Counter

if __name__ == "__main__":

    with open('input/d_03.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    commons = []
    for line in lines:
        d = len(line)//2
        a, b = line[:d], line[d:]

        cnt = Counter(''.join(set(a)) + ''.join(set(b)))
        commons.extend(
            [x for x in cnt if cnt[x] == 2]
        )

    arr = [ord(x)-ord('a')+1 if 'a' <= x <= 'z' else ord(x)-ord('A')+27 for x in commons]
    print('p1: ', sum(arr))


    commons = []
    for i in range(0, len(lines), 3):
        a, b, c = lines[i:i+3]
        cnt = Counter(''.join(set(a)) + ''.join(set(b)) + ''.join(set(c)))
        commons.extend(
            [x for x in cnt if cnt[x] == 3]
        )

    arr = [ord(x)-ord('a')+1 if 'a' <= x <= 'z' else ord(x)-ord('A')+27 for x in commons]
    print('p2: ', sum(arr))
