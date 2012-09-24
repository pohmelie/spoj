mem = {1:3, 2:9}
def yoba(n):
    if n not in mem:
        mem[n] = yoba(n - 2) + yoba(n - 1) * 2
    return mem[n]

def brute(n):
    from itertools import product, permutations
    ret = 0
    for s in product("xyz", repeat=n):
        spec = False
        for template in permutations("xyz", 3):
            if "".join(template) in "".join(s):
                spec = True
                break
        if not spec:
            ret += 1
    return ret

for _ in range(int(input())):
    n = int(input())
    print("yoba answer:", yoba(n))
    print("brute answer:", brute(n))
