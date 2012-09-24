while True:
    x = int(input())
    if x == -1:
        break
    d = 9 - 12 * (1 - x)
    print("Y" if d == (d ** 0.5) ** 2 and ((d ** 0.5) - 3) % 2 == 0 else "N")
