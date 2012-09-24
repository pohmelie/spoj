n, m = io.read("*number", "*number")
if m ~= n - 1 then
    print("NO")
else
    nodes = {}
    for _ = 1, m do
        a, b = io.read("*number", "*number")
        if nodes[a] and nodes[b] then
            print("NO")
            os.exit()
        end
        nodes[a], nodes[b] = true, true
    end
    if #nodes ~= n then
        print("NO")
    else
        print("YES")
    end
end
