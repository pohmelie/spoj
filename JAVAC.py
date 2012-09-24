while True:
    try:
        s = input()
        if s == "":
            break
        if s.islower() and "__" not in s and s[0] != "_" and s[-1] != "_":
            ws = s.split("_")
            fw, ws = ws[0], ws[1:]
            print("".join((fw,) + tuple(map(lambda x: x.capitalize(), ws))))
        elif "_" not in s and s[0].islower():
            rs = ""
            for ch in s:
                if not ch.islower():
                    rs += "_"
                rs += ch.lower()
            print(rs)
        else:
            print("Error!")
    except:
        break
