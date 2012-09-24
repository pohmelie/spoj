from itertools import product
from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    s, c = input(), defaultdict(lambda: 0)
    for i in range(len(s) - 2):
        c[s[i:i + 3]] += 1
    print(n, " ".join(map(lambda x: str(c["".join(x)]), product("TH", repeat=3))))
