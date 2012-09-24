while io.read() do
    local sub, s, c = io.read(), io.read(), 1
    while true do
        c = string.find(s, sub, c, true)
        io.write("\n")
        if not c then
            break
        end
        io.write(tostring(c - 1))
        c = c + 1
    end
end
