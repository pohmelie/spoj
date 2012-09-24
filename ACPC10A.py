while True:
    a, b, c = tuple(map(int, input().split()))
    if not (a or b or c):
        break
    if b - a == c - b and a != b:
        print("AP", c + b - a)
    else:
        print("GP", c * b // a)
