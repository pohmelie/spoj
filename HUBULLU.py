for _ in range(int(input())):
    n, c = tuple(map(int, input().split()))
    print("Airborne wins." if c == 0 else "Pagfloyd wins.")
