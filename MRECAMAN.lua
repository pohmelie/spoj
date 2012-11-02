local mem, map = {}, {}
mem[0], map[0] = 0, true

function yoba(m)
    for i = #mem + 1, m do
        local x, y = mem[i - 1] - i, mem[i - 1] + i
        if x < 0 or map[x] then
            mem[i], map[y] = y, true
        else
            mem[i], map[x] = x, true
        end
    end
    return mem[m]
end

while true do
    local m = io.read("*n")
    if m == -1 then
        break
    end
    print(yoba(m))
end
