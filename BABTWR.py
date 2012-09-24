from itertools import permutations, chain
from functools import partial


on = lambda a, b: a[1] < b[1] and a[0] < b[0] #a < b
blocks_mem = dict()

def yoba(blocks, height, i):
    height += blocks[i][2]
    yield height
    if blocks_mem[blocks[i]] < height:
        blocks_mem[blocks[i]] = height
        for c in range(i + 1, len(blocks)):
            if on(blocks[c], blocks[i]):
                yield max(yoba(blocks, height, c))

while True:
    n = int(input())
    if not n:
        break
    blocks = set()
    for _ in range(n):
        blocks |= set(filter(lambda x: x[0] >= x[1],
                             permutations(map(int, input().split()), 3)))
    blocks = sorted(blocks, reverse=True)
    blocks_mem.clear()
    for b in blocks:
        blocks_mem[b] = 0
    print(max(chain.from_iterable(map(partial(yoba, blocks, 0),
                                      range(len(blocks))))))
