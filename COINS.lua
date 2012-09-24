function yoba(n)
    if mem[n] == nil then
        x = yoba(math.floor(n / 2)) + yoba(math.floor(n / 3)) + yoba(math.floor(n / 4))
        mem[n] = math.max(n, x)
    end
    return mem[n]
end

mem = {}
mem[0] = 0
while true do
    n = io.read("*n")
    if not n then break end
    print(yoba(n))
end
