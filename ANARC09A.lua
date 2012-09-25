n = 0
while true do
    s, n, st, rep = io.read(), n + 1, 0, 0
    if string.sub(s, 1, 1) == "-" then
        break
    end
    for i = 1, #s - 1 do
        if string.sub(s, i, i) == "{" then
            st = st + 1
        elseif st == 0 then
            st, rep = 1, rep + 1
        else
            st = st - 1
        end
    end
    print(string.format("%d. %d", n, rep + st / 2))
end
