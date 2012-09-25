from operator import itemgetter


while True:
    s = input()
    if s == "*":
        break
    print("Y" if len(set(map(itemgetter(0), s.lower().split()))) == 1 else "N")
