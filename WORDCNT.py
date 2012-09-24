from itertools import groupby


for _ in range(int(input())):
    best = 0
    for _, g in groupby(input().split(), key=len):
        best = max(best, len(tuple(g)))
    print(best)
