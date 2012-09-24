from itertools import product


while True:
    n = int(input())
    if n == 0:
        break
    s, rows = input(), []
    for i in range(len(s) // n):
        sub = s[i * n:(i + 1) * n]
        rows.append(sub if i % 2 == 0 else sub[::-1])
    print("".join(rows[y][x] for x, y in product(range(n), range(len(s) // n))))
