while int(input()):
    trucks = list(map(int, input().split()))
    queue = list()
    head = 1
    for t in trucks:
        if t == head:
            head += 1
            while len(queue) and queue[-1] == head:
                head += 1
                queue.pop()
        else:
            queue.append(t)
    print("no" if len(queue) else "yes")
