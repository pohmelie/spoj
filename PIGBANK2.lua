for _ = 1, io.read("*n") do
    pew, pfw, cc = io.read("*n", "*n", "*n")
    coins, m, s = {}, {}, "This is impossible."
    for _ = 1, cc do
        coins[#coins + 1] = table.pack(io.read("*n", "*n"))
    end
    m[0] = 0
    for i = 1, pfw - pew do
        for _, c in ipairs(coins) do
            w, p = m[i - c[2]], c[1]
            m[i] = w and math.min(w + p, m[i] or w + p) or m[i]
        end
    end
    if m[pfw - pew] then
        s = string.format("The minimum amount of money in the piggy-bank is %d.", m[pfw - pew])
    end
    print(s)
end
