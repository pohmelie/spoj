from collections import defaultdict


sym = defaultdict(lambda: 0)
for _ in range(int(input())):
    sym.clear()
    for _ in range(int(input())):
        s = input()
        sym[s[0]] += 1
        sym[s[-1]] -= 1
    if sum(map(abs, sym.values())) > 2:#sum(filter(lambda x: x > 0, sym.values())) > 1:
        print("The door cannot be opened.")
    else:
        print("Ordering is possible.")
