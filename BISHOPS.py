while True:
    try:
        n = int(input())
        print((n << 1) - 2 if n != 1 else 1)
    except:
        break
