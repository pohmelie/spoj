for _ = 1, io.read("*number") do
    gc, mc = io.read("*number", "*number")
    gm, mm = 0, 0
    for _ = 1, gc do
        gm = math.max(io.read("*number"), gm)
    end
    for _ = 1, mc do
        mm = math.max(io.read("*number"), mm)
    end
    if gm >= mm then
        print("Godzilla")
    else
        print("MechaGodzilla")
    end
end
