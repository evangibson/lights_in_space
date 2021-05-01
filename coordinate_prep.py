import sys

# Hit every square on a 10 x10 grid
max_x = 1000
max_y = 1000

done_x = False
done_y = False

x_pos = 0
y_pos = 0

inter = 1

with open("coordinates.csv", "w") as c:
    # Write header
    row = "{},{}\n".format("x","y")
    c.write(row)

    while done_x is False:

        while done_y is False:

            if max_y < y_pos:
                done_y = True

            else:
                row = "{},{}\n".format(x_pos, y_pos) # DO
                c.write(row)
                print("Progress: {},{}".format(x_pos, y_pos), end="\r")
                sys.stdout.write("\033[K") # Cursor up one line
                y_pos += inter

        x_pos += inter
        if max_x < x_pos:
            done_x = True

        else:
            y_pos = 0 # Reset y
            done_y = False

    c.close()