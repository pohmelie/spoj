mem, n, t = (), int(input()), 0
while n != 1 and n not in mem:
    mem, n, t = mem + (n,), sum(map(lambda x: pow(int(x), 2), str(n))), t + 1
print(-1 if n != 1 else t)
