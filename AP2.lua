collectgarbage("stop")
for _ = 1, io.read("*n") do
    local x, y, s = io.read("*n", "*n", "*n")
    local n = 2 * s / (x + y)
    local d = (x * x - y * y) / (5 - n) / (x + y)
    local a1 = x - 2 * d
    print(n)
    local t = {}
    for i = 1, n do
        t[i], a1 = a1, a1 + d
    end
    print(table.concat(t, " "))
end
