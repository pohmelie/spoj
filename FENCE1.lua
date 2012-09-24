while true do
    l = io.read("*number")
    if l == 0 then
        break
    end
    print(string.format("%.2f", l * l / 2 / math.pi))
end
