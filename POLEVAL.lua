local i = 0
while true do
    local i, n, c, x = i + 1, io.read("*n"), {}, {}
    if n == -1 then
        break
    end
    for j = 0, n do
        c[j] = io.read("*n")
    end
    local k = io.read("*n")
    for j = 1, k do
        x[j] = io.read("*n")
    end
    print(string.format("Case %d:", i))
    for j = 1, k do
        local r, p = c[0], x[j]
        for k = 1, n do
            r = r * p + c[k]
        end
        print(r)
    end
end
