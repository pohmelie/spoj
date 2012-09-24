from itertools import combinations


def yoba(items, field, index=0):
    if not len(field):
        return 1
    return sum(map(lambda x: yoba(items, field - set(x), index + 1),
                   combinations(field & items[index][1], items[index][0])))

for _ in range(int(input())):
    count = int(input())
    default = list(map(int, input().split()))
    items = sorted(set(default), key=default.count, reverse=True)
    index = 0
    for i in range(len(items)):
        c = default.count(items[i])
        items[i] = (c, set(range(index)) | set(range(index + c, count)))
        index += c
    print(yoba(items, set(range(count))))
