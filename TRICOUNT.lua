for _ = 1, io.read("*number") do
    n = io.read("*nubmer")
    print(math.floor(0.125 * n * (n + 2) * (2 * n + 1)))
end
