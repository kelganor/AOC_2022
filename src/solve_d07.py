def imitate(lines):
    lines = lines.strip().split('\n')
    root = {'folders': {}, 'files': set()}
    tree = [root]

    for line in lines:
        if line[0] == '$':
            if line[:6] == '$ cd /':
                tree = [root]
            elif line[:7] == '$ cd ..':
                if len(tree) > 1: tree.pop()
            elif line[:4] == '$ ls':
                pass
            else: #  $ cd nxt_fldr_nm
                _, cd, t = line.split()
                if t not in tree[-1]['folders'][t]:
                    tree[-1]['folders'][t] = {'folders': {}, 'files': set()}
                tree.append(tree[-1]['folders'][t])
        else:
            a, b = line.split()
            if a != 'dir':
                tree[-1]['files'].add((int(a), b))
            else:
                if b not in tree[-1]['folders']:
                    tree[-1]['folders'][b] = {'folders': {}, 'files': []}
    calculate_sizes(root)
    return root


def calculate_sizes(root):
    res = 0
    for w, f in root['files']:
        res += w
    for subf in root['folders']:
        res += calculate_sizes(root['folders'][subf])
    root['size'] = res
    return res

def solve_p1(root):
    def sum_up(root):
        res = root['size'] if root['size'] <= 100000 else 0
        for subf in root['folders']:
            res += sum_up(root['folders'][subf])
        return res
    p1 = sum_up(root)
    return p1


def solve_p2(root):
    total = 70000000
    needed = 30000000
    free = total - root['size']
    to_delete = needed - free

    res = root['size']
    to_visit = [root]
    while to_visit:
        nxt = []
        for v in to_visit:
            for subf in v['folders']:
                nf = v['folders'][subf]
                if nf['size'] >= to_delete:
                    nxt.append(nf)
                    res = min(res, nf['size'])
        to_visit = nxt

    return res


with open('input/d_07.txt') as f:
    lines = f.read()

root = imitate(lines)
print('p1: ', solve_p1(root))
print('p2: ', solve_p2(root))