m, ends = dict(), set()
n = int(input())
for _ in range(n - 1):
    u, v = tuple(map(int, input().split()))
    for x, y in ((u, v), (v, u)):
        if x not in m:
            m[x] = {y}
            ends.add(x)
        else:
            m[x].add(y)
            ends.discard(x)

longest = 0
start = ends.pop()
for _ in range(2):
    last, path, l = {start}, m[start], 0
    while path:
        npath = set()
        for n in path:
            for nn in m[n]:
                if nn not in last:
                    npath.add(nn)
        last, path, l = path, npath, l + 1
    longest, start = max(longest, l), last.pop()
print(longest)
