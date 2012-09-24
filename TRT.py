from collections import


n, v, m = int(input()), [], 0
for _ in range(n):
    v.append(int(input()))
    if v[-1] > v[m]:
        m = len(v) - 1
l, r, s, i = m - 1, m + 1, v[m] * n, n - 1
while i != 0:
    #l, r = n - 1 if l < 0 else l, 0 if r >= n else r
    if l > 0 and (r >= n or v[l] > v[r]):
        s, l = s + v[l] * i, l - 1
    else:
        s, r = s + v[r] * i, r + 1
    i = i - 1
print(s)
