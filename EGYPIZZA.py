p = [0, 0, 0]
t = {"1/4":0, "1/2":1, "3/4":2}
for _ in range(int(input())):
    p[t[input()]] += 1
c = min(p[0], p[2])
p[0], p[2] = p[0] - c, p[2] - c
p[0], p[1] = p[0] % 2, p[1] + p[0] // 2
print(c + 1 + p[1] // 2 + max(p[0], p[1] % 2) + p[2])
