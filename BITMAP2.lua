function pp(f, n)
    for y = 1, n do
        print(table.concat(f[y], " "))
    end
end

function env(y, x)
    return {{y + 1, x}, {y - 1, x}, {y, x + 1}, {y, x - 1}}
end

for _ = 1, io.read("*n") do
    n, m = io.read("*n", "*n", "*l")
    f = {}
    f[0] = {}
    f[n + 1] = {}
    for y = 1, n do
        f[y], x = {}, 1
        for v in string.gmatch(io.read(), ".") do
            f[y][x], x = tonumber(v) ~= 0 and 0, x + 1
        end
    end
    repeat
        nochanges = true
        for y = 1, n do
            for x = 1, m do
                local min
                for _, p in ipairs(env(y, x)) do
                    ym, xm = table.unpack(p)
                    min = math.min(f[ym][xm] or n + m, min or n + m)
                end
                if (f[y][x] or n + m) > min + 1 then
                    f[y][x] = min + 1
                    nochanges = false
                end
            end
        end
    until nochanges
    pp(f, n)
end
