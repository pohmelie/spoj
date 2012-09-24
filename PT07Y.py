from collections import defaultdict


n, m = tuple(map(int, input().split()))
if m >= n:
    print("NO")
else:
    nodes = defaultdict(lambda: False)
    for _ in range(m):
        a, b = tuple(map(int, input().split()))
        if nodes[a] and nodes[b]:
            print("NO")
            break
        nodes[a] = nodes[b] = True
    else:
        print("NO" if len(nodes) < n else "YES")
