while true do
    local s, good = string.lower(io.read()), true
    if s == "*" then
        break
    end
    ch = string.sub(s, 1, 1)
    for c in string.gmatch(s, "%s(%a)") do
        if c ~= ch then
            good = false
            break
        end
    end

    if good then
        print("Y")
    else
        print("N")
    end
end
