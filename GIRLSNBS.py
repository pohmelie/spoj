from math import ceil


while True:
    g, b = tuple(map(int, input().split()))
    if g == -1:
        break
    print(ceil(max(g, b) / (min(g, b) + 1)))
