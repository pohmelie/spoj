for _ = 1, io.read("*n") do
    local n, c = io.read("*n", "*n")
    local x = {}
    for i = 1, n do
        x[i] = io.read("*n")
    end
    table.sort(x)
    local worst, best = 1, math.floor((x[n] - x[1]) / (c - 1))
    for i = 1, n - 1 do
        x[i] = x[i + 1] - x[i]
    end
    table.remove(x)
    while worst ~= best do
        local min, ind, curr = best, 1, math.floor((best + worst) / 2 + 0.5)
        for j = 1, c - 1 do
            local sum = 0
            while ind < n and sum < curr do
                ind, sum = ind + 1, sum + x[ind]
            end
            if sum < min then
                min = sum
            end
        end
        if min < curr then
            best = curr - 1
        else
            worst = curr
        end
    end
    print(best)
end
