from fractions import Fraction


while True:
    c = Fraction(int(float(input()) * 100), 100)
    if c == Fraction(0, 1):
        break
    x, d = Fraction(0, 1), 2
    while x < c:
        d, x = d + 1, x + Fraction(1, d)
    print(d - 2, "card(s)")
