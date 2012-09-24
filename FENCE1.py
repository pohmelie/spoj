from math import pi


while True:
    l = int(input())
    if l == 0:
        break
    print(round(l * l / 2 / pi, 2))
