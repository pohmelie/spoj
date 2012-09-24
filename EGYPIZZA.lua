local p = {0, 0, 0}
local t = {["1/4"] = 1, ["1/2"] = 2, ["3/4"] = 3}
for _ = 1, io.read("*n", "*l") do
    local i = t[io.read()]
    p[i] = p[i] + 1
end
local c = math.min(p[1], p[3])
p[1], p[3] = p[1] - c, p[3] - c
p[1], p[2] = p[1] % 2, p[2] + math.floor(p[1] / 2)
c = c + math.floor(p[2] / 2) + math.max(p[1], p[2] % 2) + p[3]
print(c + 1)
