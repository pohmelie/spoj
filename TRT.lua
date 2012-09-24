table.unpack = table.unpack or unpack

local n = io.read("*n")
local v, s, ns, max = {}, {}, {}, math.max
for i = 1, n do
    v[i] = io.read("*n")
    s[i] = 0
    ns[i] = 0
end
v[0], v[n + 1], s[0], s[-1], ns[0], ns[-1] = 0, 0, 0, 0, 0, 0
for i = 1, n do
    s, ns = ns, s
    for j = 0, i do
        local a, b = s[j - 1] + v[j] * i, s[j] + v[n + j - i + 1] * i
        if a > b then
            ns[j] = a
        else
            ns[j] = b
        end
    end
--    print(table.concat(ns, ", ", 0, i))
end
print(max(table.unpack(ns)))
