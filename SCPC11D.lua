while true do
    local a, b, c = io.read("*n", "*n", "*n")
    if a == 0 then
        break
    end
    a, b, c = a * a, b * b, c * c
    if a == b + c or b == c + a or c == a + b then
        print("right")
    else
        print("wrong")
    end
end
