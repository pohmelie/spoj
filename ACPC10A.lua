while true do
    a, b, c = io.read("*number", "*number", "*number")
    if a == 0 and b == 0 and c == 0 then
        break
    end
    if b - a == c - b and a ~= b then
        print(string.format("AP %d", c + b - a))
    else
        print(string.format("GP %d", c * b / a))
    end
end
