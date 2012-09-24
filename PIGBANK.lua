function yoba(coins, rw, cw, o)
    cw, o = cw or coins[1][2], o or {1}
    if cw == rw then
        return o
    elseif cw > rw then
        repeat
            cw, o[#o] = cw - coins[o[#o]][2], nil
        until #coins ~= o[#o]
        if #o == 0 then
            return nil
        end
        cw, o[#o] = cw + coins[o[#o] + 1][2], o[#o] + 1
    else
        cw, o[#o + 1] = cw + coins[o[#o]][2], o[#o]
    end
    return yoba(coins, rw, cw, o)
end

for _ = 1, io.read("*n") do
    pew, pfw, cc = io.read("*n", "*n", "*n")
    coins = {}
    for _ = 1, cc do
        coins[#coins + 1] = table.pack(io.read("*n", "*n"))
    end
    table.sort(coins, function(a, b)
        return a[1] / a[2] < b[1] / b[2]
    end)
    ret = yoba(coins, pfw - pew)
    if ret then
        local cash = 0
        for i = 1, #ret do
            cash = cash + coins[ret[i]][1]
        end
        print(string.format("The minimum amount of money in the piggy-bank is %d.", cash))
    else
        print("This is impossible.")
    end
end
