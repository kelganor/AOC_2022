from copy import deepcopy

with open('input/d_05.txt') as f:
    lines = f.read()

# format input
stacks, cmnds = lines.split('\n\n')
stacks = [list(line) for line in stacks.split('\n')]

stacks = list(zip(*stacks[::-1]))
dstacks = {
    line[0]: [x for x in list(line[1:]) if x != ' ']
    for line in stacks if line[0] != ' '
}
cmnds = [
    cmnd.replace('move ', '').replace('from ', '').replace('to ', '').split()
    for cmnd in cmnds.strip().split('\n')
]


# part 1
dst = deepcopy(dstacks)
for cmnd in cmnds:
    dn, sf, st = cmnd
    dst[st].extend(
        [dst[sf].pop() for _ in range(int(dn))]
    )

print('p1: ', ''.join([
    dst[s][-1] for s in dst
]))


# part 2
dst = deepcopy(dstacks)
for cmnd in cmnds:
    dn, sf, st = cmnd
    dst[st].extend(
        reversed([dst[sf].pop() for _ in range(int(dn))])
    )

print('p2: ',  ''.join([
    dst[s][-1] for s in dst
]))
