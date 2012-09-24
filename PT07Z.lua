n = io.read("*n")
m, ends = {}, {}
for _ = 1, n - 1 do
    u, v = io.read("*n", "*n")
    function yoba(x, y)
        if m[x] == nil then
            m[x] = {y}
            ends[x] = true
        else
            m[x][#m[x] + 1] = y
            ends[x] = nil
        end
    end
    yoba(u, v)
    yoba(v, u)
end

longest = 0
for i, _ in pairs(ends) do
    start = i
    break
end

last, path, l = {start}, m[start], 0
for _ = 1, 2 do
    while #path ~= 0 do
        npath, nlast = {}, {}
        for _, v in pairs(last) do
            nlast[v] = true
        end
        last = nlast
        for _, n in pairs(path) do
            for _, nn in pairs(m[n]) do
                if last[nn] == nil then
                    npath[#npath + 1] = nn
                end
            end
        end
        last, path, l = path, npath, l + 1
    end
    longest = math.max(longest, l)
    last, path, l = {last[1]}, m[last[1]], 0
end
print(longest)
