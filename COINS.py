def yoba(n):
    if n not in mem:
        mem[n] = max(n, sum(map(lambda x: yoba(n // x), range(2, 5))))
    return mem[n]

mem = {0:0}
while True:
    try:
        print(yoba(int(input())))
    except:
        break
