local mem = {1}
local function yoba(x)
    if not mem[x] then
        for i = #mem + 1, x do
            mem[i] = 1 + mem[i - 1] * i / (i - 1)
        end
    end
    return mem[x]
end

for _ = 1, io.read("*n") do
    print(string.format("%.2f", yoba(io.read("*n"))))
end
