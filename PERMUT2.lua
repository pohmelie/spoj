while true do
    n = io.read("*number")
    if n == 0 then
        break
    end
    x = {}
    for i = 1, n do
        x[i] = io.read("*nubmer")
    end
    f = false
    for i = 1, n do
        if x[x[i]] ~= i then
            f = true
            break
        end
    end
    if f then
        print("not ambiguous")
    else
        print("ambiguous")
    end
end
