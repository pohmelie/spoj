while True:
    s = input()
    if s == "00e0":
        break
    m, e = tuple(map(int, s.split("e")))
    start, stop, step, carry = 1, m * pow(10, e), 1, 0
    while start + step - 1 <= stop:
        start, step, carry = start + carry * step, step * 2, ((stop - start) // step + 1) % 2 ^ carry
    print(start)
