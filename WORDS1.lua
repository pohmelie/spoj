local i, o = {}, {}
for _ = 1, io.read("*n", "*l") do
    for i = 1, io.read("*n", "*l") do
        local s = io.read()
        local f, l = string.byte(s) - 96, string.byte(s, #s) - 96
        i[f] = (i[f] or 0) + 1
        o[l] = (o[l] or 0) + 1
    end
    local s = 0
    for i = 1, 26 do
        s = s + math.abs(sym[i] or 0)
        sym[i] = 0
    end
    if s > 2 then
        print("The door cannot be opened.")
    else
        print("Ordering is possible.")
    end
end
