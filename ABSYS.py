for _ in range(int(input())):
    input()
    el = input().split()
    if not el[0].isnumeric():
        el[0] = str(int(el[4]) - int(el[2]))
    elif not el[2].isnumeric():
        el[2] = str(int(el[4]) - int(el[0]))
    else:
        el[4] = str(int(el[0]) + int(el[2]))
    print(" ".join(el))
