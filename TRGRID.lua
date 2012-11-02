for _ = 1, io.read("*n") do
    h, w = io.read("*n"), io.read("*n")
    if h > w then
        if w % 2 == 1 then
            print("D")
        else
            print("U")
        end
    elseif h <= w then
        if h % 2 == 1 then
            print("R")
        else
            print("L")
        end
    end
end
