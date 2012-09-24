from operator import floordiv, mul, add, sub

ops = {"+":add, "-":sub, "*":mul, "/":floordiv}
for _ in range(int(input())):
    input()
    n, op = 0, add
    for w in input().split():
        if w == "=":
            break
        elif w.isdigit():
            n = op(n, int(w))
        else:
            op = ops[w]
    print(n)
