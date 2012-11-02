local function _in(d, x)
    for i = 1, #d do
        if d[i] == x then
            return true
        end
    end
    return false
end

while true do
    local n = io.read("*n")
    local g = {}
    if n == 0 then
        break
    end
    local m = io.read("*n")
    for _ = 1, m do
        local a, b, p = io.read("*n", "*n", "*n")
        g[a] = g[a] or {}
        g[a][b] = p / 100
        g[b] = g[b] or {}
        g[b][a] = p / 100
    end

    local curr_path, curr_weight, best_weight, s = {1}, 0, nil, 1
    while s ~= n do
        for i = 1, #curr_path do
            io.write(string.format("%d, ", curr_path[i]))
        end
        print()
        print(curr_weight, best_weight)
        for i = s + 1, n do
            if g[s] and g[s][i] and not _in(curr_path, i) then
                local new_weight = curr_weight * g[s][i]
                if (not best_weight) or new_weight > best_weight then
                    if i == n then
                        best_weight = new_weight
                    else
                        curr_weight = new_weight
                        curr_path[#curr_path + 1] = i
                        s = 1
                        break
                    end
                end
            end
            if i == n then
                s = curr_path[#curr_path] + 1
                curr_path[#curr_path] = nil
            end
        end
    end
    print(string.format("%.6f", best_weight * 100))
end
