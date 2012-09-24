from itertools import product


for _ in range(int(input())):
    w, h = tuple(map(int, input().split()))
    wall = ("#" * (w + 2),)
    walkers = nwalkers = None
    field = wall + tuple(map(lambda _: "#" + input() + "#", range(h))) + wall
    neighbour = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

    for i, j in product(range(1, w + 1), range(1, h + 1)):
        if field[j][i] == "." and sum((1 for x, y in neighbour(i, j) if field[y][x] == ".")) < 2:
            nwalkers = ((0, None, (i, j)),)
            break

    rope = 0
    while nwalkers:
        walkers, nwalkers = nwalkers, ()
        for weight, prev, curr in walkers:
            steps = tuple(filter(
                lambda p: field[p[1]][p[0]] == "." and p != prev,
                neighbour(*curr)))
            nwalkers += tuple(map(lambda s: (weight + 1, curr, s), steps))
            rope = max(weight, rope)

    print("Maximum rope length is {}.".format(rope))
