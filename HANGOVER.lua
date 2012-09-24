mem = {}
for i = 1, 276 do
    mem[i] = (mem[i - 1] or 0) + 1 / (i + 1)
end

while true do
    x = io.read("*number")
    if x == 0 then
        break
    end
    for i = 1, 276 do
        if mem[i] > x then
            print(string.format("%d card(s)", i))
            break
        end
    end
end
