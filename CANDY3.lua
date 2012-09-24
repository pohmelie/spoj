for _ = 1, io.read("*number") do
    n, s = io.read("*number"), 0
    for _ = 1, n do
        s = s + io.read("*number")
        if s % n == 0 then
            s = 0
        end
    end
    if s % n == 0 then
        print("YES")
    else
        print("NO")
    end
end
