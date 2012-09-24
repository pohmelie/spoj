local mem, i = {}, 0
repeat
    i, mem[i] = i + 1, 3 * i * (i + 1) + 1
until mem[i - 1] > 1000000000

while true do
    local x = io.read("*n")
    if x == -1 then
        break
    end
    local low, high = 0, #mem
    while low ~= high do
        local mid = math.floor((low + high) / 2 +0.5)
        if x < mem[mid] then
            high = mid - 1
        else
            low = mid
        end
    end
    if mem[high] ~= x then
        print("N")
    else
        print("Y")
    end
end
