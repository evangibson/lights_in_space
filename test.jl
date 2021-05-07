# Write header

for x in 0:10000
    for y in 0:100
        x = x * 1
        y = y * 1
        row = "$(x)"  # DO
        print("Progress: $(row) \r")
        flush(stdout)
        
    end
end