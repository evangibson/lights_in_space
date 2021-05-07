# Write header

for q in 0:100000
    for a in 0:100000
        x = q * 0.001
        y = a * 0.001
        row = "$(x)         ,$(y)  "  # DO
        print("Progress: $(row) \r")
        flush(stdout)
        
    end
end