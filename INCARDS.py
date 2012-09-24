from collections import defaultdict
import sys

def step(nodes, src, dst, path=[], cost=0, current_best=None):
    if src == dst:
        return cost
    for d, p in nodes[src]:
        if d not in path:
            if not current_best or cost + p < current_best:
                path.append(src)
                current_best = step(nodes, d, dst, path, cost + p, current_best)
                path.pop()
    return current_best

sys.setrecursionlimit(1000)
c = int(input())
inp = lambda: tuple(map(int, input().split()))
while c:
    c -= 1
    p, q = inp()
    nodes = defaultdict(list)
    for i in range(q):
        o, d, p = inp()
        nodes[o].append((d, p))
    print(sum(map(lambda dst: step(nodes, 1, dst) + step(nodes, dst, 1), nodes)))
