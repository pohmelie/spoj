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
    f, front = {}, {}
    for y = 1, n do
        f[y], x = {}, 1
        for v in string.gmatch(io.read(), ".") do
            if tonumber(v) ~= 0 then
                f[y][x], front[#front + 1] = 0, {y, x}
            end
            x = x + 1
        end
    end
    repeat
        _front, front, nochanges = front, {}, true
        for _, p in ipairs(_front) do
            y, x = table.unpack(p)
            for _, p in ipairs(env(y, x)) do
                yn, xn = table.unpack(p)
                if 0 < yn and yn <= n and 0 < xn and xn <= m and f[yn][xn] == nil then
                    local min = n + m
                    for _, p in ipairs(env(yn, xn)) do
                        ym, xm = table.unpack(p)
                        if 0 < ym and ym <= n and 0 < xm and xm <= m then
                            min = math.min(f[ym][xm] or n + m, min)
                        end
                    end
                    f[yn][xn], front[#front + 1], nochanges = min + 1, {yn, xn}, false
                end
            end
        end
    until nochanges
    pp(f, n)
end
