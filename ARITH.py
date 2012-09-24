for _ in range(int(input())):
    s = input()
    if "+" in s:
        a, b = tuple(s.split("+"))
        c = str(int(a) + int(b))
        longest = max(len(c), len(b) + 1)
        print((longest - len(a)) * " " + a)
        print((longest - len(b) - 1) * " " + "+" + b)
        print(longest * "-")
        print((longest - len(c)) * " " + c)
    elif "-" in s:
        a, b = tuple(s.split("-"))
        c = str(int(a) - int(b))
        longest = max(len(c), len(b) + 1, len(a))
        print((longest - len(a)) * " " + a)
        print((longest - len(b) - 1) * " " + "-" + b)
        linelen = max(len(c), len(b) + 1)
        print((longest - linelen) * " " + linelen * "-")
        print((longest - len(c)) * " " + c)
    else:
        a, b = tuple(s.split("*"))
        ai, bi = int(a), int(b)
        precalcs = list(map(lambda n: str(ai * int(n)), reversed(b)))
        c = str(ai * bi)

        totallen = max(len(a), len(b) + 1, len(c))
        startlinelen = max(len(b) + 1, len(precalcs[0]))
        endlinelen = max(len(precalcs) - 1 + len(precalcs[-1]), len(c))

        print((totallen - len(a)) * " " + a)
        print((totallen - len(b) - 1) * " " + "*" + b)
        print((totallen - startlinelen) * " " + startlinelen * "-")
        precalcs_shift = 0
        for prec in precalcs:
            print((totallen - precalcs_shift - len(prec)) * " " + prec)
            precalcs_shift += 1
        if len(precalcs) != 1:
            print((totallen - endlinelen) * " " + endlinelen * "-")
            print((totallen - len(c)) * " " + c)
    print()
