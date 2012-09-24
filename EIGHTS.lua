nums = {192, 442, 692, 942}
for _ = 1, io.read("*number") do
    k = io.read("*number")
    k, i = math.floor((k - 1) / 4), (k - 1) % 4
    if k ~= 0 then
        io.write(k)
    end
    print(nums[i + 1])
end
