local i = 0
while true do
    local i, n, c, x = i + 1, io.read("*n"), {}, {}
    if n == -1 then
        break
    end
    for j = n, 1, -1 do
        c[j] = io.read("*n")
    end
    local c0 = io.read("*n")
    local k = io.read("*n")
    for j = 1, k do
        x[j] = io.read("*n")
    end
    print(string.format("Case %d:", i))
    for _, p in ipairs(x) do
        local r, d, mp = c0, 1, math.pow
        for _, k in ipairs(c) do
            r, d = r + k * mp(p, d), d + 1
        end
        print(r)
    end
end
